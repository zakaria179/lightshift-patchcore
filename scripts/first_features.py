from pathlib import Path
import torch
import torchvision.models as models
import torchvision.transforms as T
from PIL import Image

# 1. Load the pre-trained network (downloads ~130 MB the first time)
weights = models.Wide_ResNet50_2_Weights.IMAGENET1K_V1
net = models.wide_resnet50_2(weights=weights).eval()

# 2. Load one normal hazelnut image and prepare it for the network
folder = Path("data/mvtec_anomaly_detection/hazelnut/train/good")
img = Image.open(sorted(folder.glob("*.png"))[0]).convert("RGB")
prepare = T.Compose([
    T.Resize(256),
    T.CenterCrop(224),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
x = prepare(img).unsqueeze(0)   # shape: (1 image, 3 colors, 224, 224)
print("image tensor:", tuple(x.shape))

# 3. Run the image through the network, stopping at layer2 and layer3
with torch.no_grad():
    x = net.maxpool(net.relu(net.bn1(net.conv1(x))))
    x = net.layer1(x)
    f2 = net.layer2(x)
    f3 = net.layer3(f2)

print("layer2 features:", tuple(f2.shape))
print("layer3 features:", tuple(f3.shape))
print("first patch of layer2 (first 8 numbers):", f2[0, :8, 0, 0])
