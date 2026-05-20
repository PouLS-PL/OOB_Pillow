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
    image_path = create_pattern_image(tmp_path / "perf_pattern.jpg")

    with Image.open(image_path) as image:
        def apply_blur():
            image.filter(ImageFilter.GaussianBlur(radius=5))

        benchmark(apply_blur)
