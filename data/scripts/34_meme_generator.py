import tempfile
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


def _load_font(size: int):
    for name in ("DejaVuSans-Bold.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _draw_centered(draw, text: str, font, y: int, width: int) -> None:
    text = text.upper()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = max((width - text_width) // 2, 0)
    for dx in (-2, 2):
        for dy in (-2, 2):
            draw.text((x + dx, y + dy), text, font=font, fill="black")
    draw.text((x, y), text, font=font, fill="white")


def make_meme(template: Path, top: str, bottom: str, output: Path) -> Path:
    image = Image.open(template).convert("RGB")
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font = _load_font(max(height // 10, 14))
    _draw_centered(draw, top, font, 10, width)
    _draw_centered(draw, bottom, font, height - height // 8, width)
    image.save(output)
    return output


def main() -> None:
    if not HAS_PIL:
        print("Pillow не установлен. Установите: pip install Pillow")
        return
    tmp = Path(tempfile.mkdtemp())
    template = tmp / "template.png"
    Image.new("RGB", (500, 400), color=(70, 130, 180)).save(template)

    output = make_meme(template, "Когда код работает", "Но ты не знаешь почему", tmp / "meme.png")
    print(f"Мем создан: {output}")
    print(f"Размер файла: {output.stat().st_size} байт")


if __name__ == "__main__":
    main()
