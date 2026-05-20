from PIL import Image

from tests.helpers import create_test_image


def test_generate_thumbnail_preserves_aspect_ratio(tmp_path):
    """Realny scenariusz: generowanie miniatury z zachowaniem proporcji obrazu."""
    image_path = create_test_image(tmp_path / "thumbnail_input.png", size=(1200, 800), color=(10, 20, 30))
    with Image.open(image_path) as image:
        image.thumbnail((400, 400))
        assert max(image.size) == 400
        assert image.size == (400, 267)
