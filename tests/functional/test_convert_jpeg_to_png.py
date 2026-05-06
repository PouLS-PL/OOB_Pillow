from PIL import Image

from tests.helpers import create_test_image


def test_convert_jpeg_to_png_preserves_dimensions(tmp_path):
    """Realny scenariusz: konwersja obrazu do innego formatu przy zachowaniu rozmiaru."""
    input_path = create_test_image(tmp_path / "input.jpeg", size=(640, 480))
    with Image.open(input_path) as source:
        assert source.format == "JPEG"
        output_path = tmp_path / "output.png"
        source.save(output_path, format="PNG")

    with Image.open(output_path) as output:
        assert output.format == "PNG"
        assert output.size == (640, 480)
