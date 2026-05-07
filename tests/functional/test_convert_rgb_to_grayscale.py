from PIL import Image

from tests.helpers import create_test_image


def test_convert_rgb_to_grayscale_changes_mode(tmp_path):
    """Realny scenariusz: konwersja obrazu do czarno-białej wersji w aplikacji."""
    image_path = create_test_image(tmp_path / "rgb_input.png", size=(200, 200), color=(125, 200, 75))
    with Image.open(image_path) as image:
        converted = image.convert("L")
        assert converted.mode == "L"
