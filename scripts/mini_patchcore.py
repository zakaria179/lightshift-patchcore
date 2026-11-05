import random
from pathlib import Path

import torch
import torch.nn.functional as F
import torchvision.models as models
import torchvision.transforms as T
from PIL import Image
from sklearn.metrics import roc_auc_score
from tqdm import tqdm

CATEGORY = "hazelnut"   # change this to try another category
N_TRAIN = 40            # number of normal images used for the memory bank
root = Path("data/mvtec_anomaly_detection") / CATEGORY

# Pre-trained network (same as before)
net = models.wide_resnet50_2(weights=models.Wide_ResNet50_2_Weights.IMAGENET1K_V1).eval()
prepare = T.Compose([
    T.Resize(256),
    T.CenterCrop(224),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


@torch.no_grad()
def patch_features(path):
    """Return one row of 1536 numbers per patch: shape (784, 1536)."""
    x = prepare(Image.open(path).convert("RGB")).unsqueeze(0)
    x = net.maxpool(net.relu(net.bn1(net.conv1(x))))
    x = net.layer1(x)
    f2 = net.layer2(x)
    f3 = net.layer3(f2)
    f3 = F.interpolate(f3, size=f2.shape[-2:], mode="bilinear", align_corners=False)
    f = torch.cat([f2, f3], dim=1)      # (1, 1536, 28, 28)
    return f[0].flatten(1).T            # (784, 1536)


# Step 1: build the memory bank from normal training images
train_paths = sorted((root / "train" / "good").glob("*.png"))
train_paths = random.Random(0).sample(train_paths, N_TRAIN)
bank = torch.cat([patch_features(p) for p in tqdm(train_paths, desc="memory bank")])
print("memory bank shape:", tuple(bank.shape))


# Step 2: score a test image = largest distance to the nearest normal patch
@torch.no_grad()
def anomaly_score(path):
    patches = patch_features(path)
    dist = torch.cdist(patches, bank)       # (784, bank size)
    nearest = dist.min(dim=1).values        # closest normal patch for each patch
    return nearest.max().item()


# Step 3: score all test images (label 0 = normal, 1 = defective)
scores, labels = [], []
for folder in sorted((root / "test").iterdir()):
    label = 0 if folder.name == "good" else 1
    for p in tqdm(sorted(folder.glob("*.png")), desc=f"test/{folder.name}"):
        scores.append(anomaly_score(p))
        labels.append(label)

normal = [s for s, l in zip(scores, labels) if l == 0]
defect = [s for s, l in zip(scores, labels) if l == 1]
print(f"average score, normal images   : {sum(normal) / len(normal):.2f}")
print(f"average score, defective images: {sum(defect) / len(defect):.2f}")
print(f"image AUROC: {roc_auc_score(labels, scores):.3f}")
