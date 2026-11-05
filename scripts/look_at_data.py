from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image

root = Path("data/mvtec_anomaly_detection/hazelnut")
train = sorted((root / "train" / "good").glob("*.png"))
print("normal train images:", len(train))
for d in sorted((root / "test").iterdir()):
    print(d.name, len(list(d.glob("*.png"))))

defect_dir = next(d for d in sorted((root / "test").iterdir()) if d.name != "good")
img_path = sorted(defect_dir.glob("*.png"))[0]
mask_path = root / "ground_truth" / defect_dir.name / (img_path.stem + "_mask.png")

fig, ax = plt.subplots(1, 3, figsize=(12, 4))
ax[0].imshow(Image.open(train[0]));            ax[0].set_title("normal (train)")
ax[1].imshow(Image.open(img_path));            ax[1].set_title(f"defect: {defect_dir.name}")
ax[2].imshow(Image.open(mask_path), cmap="gray"); ax[2].set_title("ground-truth mask")
for a in ax:
    a.axis("off")
plt.savefig("results/first_look.png", dpi=100, bbox_inches="tight")
