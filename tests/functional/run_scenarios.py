from io import BytesIO

from PIL import Image


def run_pt_01() -> bool:
    source = Image.new("RGB", (64, 32), color="white")

    input_buffer = BytesIO()
    source.save(input_buffer, format="JPEG")
    input_buffer.seek(0)

    loaded = Image.open(input_buffer)
    output_buffer = BytesIO()
    loaded.save(output_buffer, format="PNG")
    output_buffer.seek(0)

    result = Image.open(output_buffer)
    return result.format == "PNG" and result.size == source.size


if __name__ == "__main__":
    print("PASS" if run_pt_01() else "FAIL")