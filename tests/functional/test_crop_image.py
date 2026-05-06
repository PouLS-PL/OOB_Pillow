from PIL import Image

from tests.helpers import create_test_image


def test_crop_image_extracts_expected_region(tmp_path):
    """Realny scenariusz: wycinanie fragmentu obrazu do dalszej obróbki lub analizy."""
    image_path = create_test_image(tmp_path / "crop_input.png", size=(800, 600), color=(0, 120, 255))
    with Image.open(image_path) as image:
        cropped = image.crop((100, 100, 400, 300))
        assert cropped.size == (300, 200)
        assert cropped.getpixel((0, 0)) == image.getpixel((100, 100))
