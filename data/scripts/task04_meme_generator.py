import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

_FONT_CANDIDATES = (
    "Impact.ttf",
    "DejaVuSans-Bold.ttf",
    "LiberationSans-Bold.ttf",
    "Arial.ttf",
)


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for name in _FONT_CANDIDATES:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _draw_centered(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.ImageFont,
    image_width: int,
    top: int,
    stroke: int,
) -> None:
    left, _, right, _ = draw.textbbox((0, 0), text, font=font, stroke_width=stroke)
    x = (image_width - (right - left)) / 2
    draw.text(
        (x, top),
        text,
        font=font,
        fill="white",
        stroke_width=stroke,
        stroke_fill="black",
    )


def generate_meme(template: Path, top_text: str, bottom_text: str, output: Path) -> Path:
    image = Image.open(template).convert("RGB")
    draw = ImageDraw.Draw(image)
    font = _load_font(max(20, image.width // 10))
    stroke = max(1, image.width // 200)
    margin = image.height // 20

    if top_text:
        _draw_centered(draw, top_text.upper(), font, image.width, margin, stroke)
    if bottom_text:
        text = bottom_text.upper()
        _, top, _, bottom = draw.textbbox((0, 0), text, font=font, stroke_width=stroke)
        y = image.height - (bottom - top) - margin
        _draw_centered(draw, text, font, image.width, y, stroke)

    image.save(output)
    return output


def main() -> None:
    if len(sys.argv) != 5:
        name = Path(sys.argv[0]).name
        print(f"Использование: {name} <шаблон> <верхний текст> <нижний текст> <выход>", file=sys.stderr)
        raise SystemExit(2)
    template = Path(sys.argv[1])
    if not template.is_file():
        print(f"Шаблон не найден: {template}", file=sys.stderr)
        raise SystemExit(1)
    output = generate_meme(template, sys.argv[2], sys.argv[3], Path(sys.argv[4]))
    print(f"Мем сохранён: {output.resolve()}")


if __name__ == "__main__":
    main()
