import time

from PIL import Image, ImageFilter

from tests.helpers import create_pattern_image

#this function is not needed anymore- pytest-benchmark will replace it (at least i hope so)

# def _average_duration(operation, iterations=3):
#     durations = []
#     for _ in range(iterations):
#         start = time.perf_counter()
#         operation()
#         durations.append(time.perf_counter() - start)
#     return sum(durations) / len(durations)




def test_gaussian_blur_performance(tmp_path, benchmark):
    """Realny scenariusz: pomiar czasu zastosowania filtra przy przetwarzaniu obrazu."""
    image_path = create_pattern_image(tmp_path / "perf_pattern.jpg")

    with Image.open(image_path) as image:
        def apply_blur():
            image.filter(ImageFilter.GaussianBlur(radius=5))

        avg_duration = _average_duration(apply_blur)
        print(f"PERF: gaussian blur average = {avg_duration:.3f}s")
        assert avg_duration < 1.0
