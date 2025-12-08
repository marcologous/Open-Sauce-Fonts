"""Generate a specimen image for a TrueType font.

This script renders the word 'Hamburgivots' in 100px size using a provided
TTF font file. The output image is saved as ``specimen.png`` in the current
working directory.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

TEXT = "Hamburgivots"
FONT_SIZE = 100
TEXT_COLOR = "black"
BACKGROUND_COLOR = "white"
OUTPUT_FILE = "specimen.png"
PADDING = 20


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Render the word 'Hamburgivots' in black on a white background "
            "using the provided TTF font and save it as specimen.png."
        )
    )
    parser.add_argument(
        "font_path",
        type=Path,
        help="Path to the TTF font file to use for rendering the specimen.",
    )
    return parser.parse_args()


def validate_font(font_path: Path) -> None:
    """Load the font using fontTools to ensure it's a valid TTF file."""
    try:
        TTFont(font_path)
    except Exception as exc:  # pragma: no cover - defensive guard
        raise SystemExit(f"Unable to load font '{font_path}': {exc}") from exc


def render_specimen(font_path: Path) -> Path:
    validate_font(font_path)
    font = ImageFont.truetype(str(font_path), FONT_SIZE)

    dummy_image = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy_image)
    bbox = draw.textbbox((0, 0), TEXT, font=font)

    width = bbox[2] - bbox[0] + PADDING * 2
    height = bbox[3] - bbox[1] + PADDING * 2

    image = Image.new("RGB", (width, height), color=BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)
    draw.text((PADDING, PADDING), TEXT, fill=TEXT_COLOR, font=font)

    output_path = Path(OUTPUT_FILE)
    image.save(output_path)
    return output_path


def main() -> None:
    args = parse_args()
    output = render_specimen(args.font_path)
    print(f"Specimen saved to {output.resolve()}")


if __name__ == "__main__":
    main()
