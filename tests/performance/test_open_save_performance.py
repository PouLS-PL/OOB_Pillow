import time

from PIL import Image

from tests.helpers import create_test_image


def _average_duration(operation, iterations=3):
    durations = []
    for _ in range(iterations):
        start = time.perf_counter()
        operation()
        durations.append(time.perf_counter() - start)
    return sum(durations) / len(durations)


def test_open_save_performance(tmp_path):
    """Realny scenariusz: pomiar czasu odczytu i zapisu obrazu w systemie przetwarzania.
    """
    image_path = create_test_image(tmp_path / "perf_input.jpg", size=(1200, 1200))

    def open_save():
        with Image.open(image_path) as image:
            image.save(tmp_path / "perf_output.png", format="PNG")

    avg_duration = _average_duration(open_save)
    print(f"PERF: open+save average = {avg_duration:.3f}s")
    assert avg_duration < 1.5
