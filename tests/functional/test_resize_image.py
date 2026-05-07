from PIL import Image

from tests.helpers import create_test_image


def test_resize_image_changes_image_size(tmp_path):
    """Realny scenariusz: zmiana rozmiaru obrazu do wersji zoptymalizowanej dla UI lub miniatur."""
    image_path = create_test_image(tmp_path / "resize_input.png", size=(1000, 1000), color=(0, 255, 0))
    with Image.open(image_path) as image:
        resized = image.resize((500, 500))
        assert resized.size == (500, 500)
