import pytest

from PIL import Image, ImageFilter, UnidentifiedImageError

from tests.helpers import create_test_image


def test_open_nonexistent_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        Image.open(tmp_path / "no_such.jpg")


def test_open_corrupt_image_raises_unidentified_error(tmp_path):
    p = tmp_path / "corrupt.jpg"
    p.write_bytes(b"this is not a valid image file")
    with pytest.raises(UnidentifiedImageError):
        with Image.open(p) as im:
            im.load()


def test_save_with_invalid_format_raises_value_error(tmp_path):
    img_path = create_test_image(tmp_path / "valid.png")
    with Image.open(img_path) as img:
        with pytest.raises(ValueError):
            img.save(tmp_path / "out.invalid", format="INVALID_FORMAT")


def test_resize_with_negative_dimensions_raises_value_error(tmp_path):
    img_path = create_test_image(tmp_path / "resize.png")
    with Image.open(img_path) as img:
        with pytest.raises(ValueError):
            img.resize((-10, -10))


def test_convert_with_invalid_mode_raises_value_error(tmp_path):
    img_path = create_test_image(tmp_path / "convert.png")
    with Image.open(img_path) as img:
        with pytest.raises(ValueError):
            img.convert("INVALID_MODE")


def test_filter_with_invalid_radius_type_raises_type_error(tmp_path):
    img_path = create_test_image(tmp_path / "filter.png")
    with Image.open(img_path) as img:
        with pytest.raises(TypeError):
            img.filter(ImageFilter.GaussianBlur(radius="not_a_number"))


def test_operation_on_closed_image_raises_value_error(tmp_path):
    img_path = create_test_image(tmp_path / "closed.png")
    img = Image.open(img_path)
    img.close()
    with pytest.raises(ValueError):
        img.filter(ImageFilter.GaussianBlur(radius=2))
