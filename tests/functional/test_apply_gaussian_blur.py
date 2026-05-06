from PIL import Image, ImageFilter

from tests.helpers import create_pattern_image, checksum


def test_apply_gaussian_blur_modifies_pixel_data(tmp_path):
    """Realny scenariusz: modyfikacja obrazu przy użyciu filtra w aplikacji graficznej."""
    image_path = create_pattern_image(tmp_path / "filter_input.jpg")
    with Image.open(image_path) as original:
        blurred = original.filter(ImageFilter.GaussianBlur(radius=5))
        assert checksum(original) != checksum(blurred)
        assert blurred.size == original.size
