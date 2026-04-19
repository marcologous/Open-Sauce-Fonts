# Open Sauce Fonts

A contemporary grotesque superfamily designed by [Alfredo Marco Pradil](https://www.behance.net/pradil) for [Creative Sauce](https://www.behance.net/creativesauceagency).

## Overview

Open Sauce Fonts is a versatile type family optimized for digital interfaces, branding, and editorial design. The family comprises three distinct variants—each with unique optical characteristics while maintaining visual consistency across weights and styles.

## Families

| Family | Description | Characteristics |
|--------|-------------|-----------------|
| **Open Sauce Sans** | Standard grotesque with ink traps | Optimized for UI, display text |
| **Open Sauce One** | Clean grotesque without ink traps | Neutral, editorial-appropriate |
| **Open Sauce Two** | Rounded variant | Soft, approachable aesthetic |

## Technical Specifications

### Weights & Styles
- **7 weights**: Light (300), Regular (400), Medium (500), SemiBold (600), Bold (700), ExtraBold (800), Black (900)
- **2 styles per weight**: Upright and Italic
- **Total**: 42 font files per format (36 unique styles × 2 formats)

### Formats
- **OTF** (OpenType CFF): Desktop publishing, print
- **TTF** (TrueType): Web, digital distribution

### Glyph Coverage
- **358 glyphs** per font
- Extended Latin character set
- Full punctuation and symbol support

### OpenType Features
Standard features included:
- `liga` – Standard Ligatures
- `kern` – Kerning
- `smcp` – Small Capitals
- `onum` – Oldstyle Figures
- `lnum` – Lining Figures

## Installation

### macOS
```bash
# Option 1: Double-click font file → Install Font
# Option 2: Copy to ~/Library/Fonts/
cp fonts/otf/*.otf ~/Library/Fonts/
```

### Linux
```bash
# User installation
cp fonts/otf/*.otf ~/.local/share/fonts/
fc-cache -f -v

# System-wide installation (requires sudo)
sudo cp fonts/otf/*.otf /usr/share/fonts/
sudo fc-cache -f -v
```

### Windows
```bash
# Right-click font file → Install
# Or: Copy to C:\Windows\Fonts\
```

## Web Usage

### CSS Declaration
```css
@font-face {
  font-family: 'Open Sauce Sans';
  src: url('fonts/ttf/OpenSauceSans-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'Open Sauce Sans';
  src: url('fonts/ttf/OpenSauceSans-Italic.ttf') format('truetype');
  font-weight: 400;
  font-style: italic;
}
```

## Build from Source

The font sources are stored in Glyphs format in the `Source/` directory. To rebuild:

```bash
# Install dependencies
pip install fontmake glyphsLib

# Build static TTF fonts
fontmake -o ttf -i "Source/Open Sauce One.glyphs"

# Build static OTF fonts
fontmake -o otf -i "Source/Open Sauce One.glyphs"
```

## Quality Assurance

This project uses [FontBakery](https://github.com/googlefonts/fontbakery) for automated quality checks. The GitHub Actions workflow runs on every push and pull request.

```bash
# Run FontBakery locally
pip install fontbakery
fontbakery check-universal fonts/ttf/*.ttf
```

## License

Open Sauce Fonts are released under the [SIL Open Font License (OFL)](https://scripts.sil.org/OFL) version 1.1.

- Free for personal and commercial use
- No attribution required (though appreciated)
- Modifications permitted with restrictions

See individual OFL.txt files for complete license terms.

## Repository Structure

```
Open-Sauce-Fonts/
├── Source/                 # Glyphs source files
│   ├── Open Sauce One.glyphs
│   ├── Open Sauce Sans.glyphs
│   └── Open Sauce Two.glyphs
├── fonts/
│   ├── otf/               # OpenType fonts
│   └── ttf/               # TrueType fonts
├── Images/                # Specimen images
├── README.md
└── *.OFL.txt              # License files
```

## Version History

### v1.0 (Current)
- Initial release
- 3 families × 7 weights × 2 styles
- OTF and TTF formats

## Author

**Alfredo Marco Pradil**
- [Behance](https://www.behance.net/pradil)
- [GitHub](https://github.com/marcologous)

## Contributing

Issues and pull requests are welcome. Please ensure any contributions pass FontBakery checks before submitting.

---

*Open Sauce Fonts – Crafted for clarity, designed for impact.*