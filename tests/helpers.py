import hashlib
from pathlib import Path

from PIL import Image, ImageDraw


def create_test_image(path: Path, size=(1000, 1000), mode="RGB", color=(255, 0, 0)) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new(mode, size, color=color)
    fmt = "JPEG" if path.suffix.lower() in {".jpg", ".jpeg"} else "PNG"
    image.save(path, format=fmt)
    return path


def create_pattern_image(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", (200, 200), color=(0, 0, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle([50, 50, 150, 150], fill=(255, 0, 0))
    image.save(path, format="JPEG")
    return path


def checksum(image: Image.Image) -> str:
    return hashlib.sha256(image.tobytes()).hexdigest()
