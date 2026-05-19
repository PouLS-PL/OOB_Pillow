from PIL import Image

from tests.helpers import create_test_image

#this function is not needed anymore- pytest-benchmark will replace it (at least i hope so)

# def _average_duration(operation, iterations=3):
#     durations = []
#     for _ in range(iterations):
#         start = time.perf_counter()
#         operation()
#         durations.append(time.perf_counter() - start)
#     return sum(durations) / len(durations)

def test_open_save_performance(tmp_path, benchmark):
    image_path = create_test_image(tmp_path / "perf_input.jpg", size=(1200, 1200))

    def open_save():
        with Image.open(image_path) as image:
            image.save(tmp_path / "perf_output.png", format="PNG")

    benchmark(open_save)
