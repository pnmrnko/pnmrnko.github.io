#!/usr/bin/env python3
"""Build the New Computer Modern web fonts from TeX Live.

Text faces (Serif, Sans, Mono) are cut into WOFF2 subsets by script with
matching unicode-range rules, so a browser downloads only the pieces a page
uses: a Ukrainian page fetches the Latin and Cyrillic files of the faces it
needs, nothing else. Math faces stay whole, because their OpenType MATH
table points at glyph variants and assembly parts that no codepoint reaches.

Writes static/fonts/newcm/*.woff2 and assets/scss/_fonts.scss.

    python3 tools/build-fonts.py [path/to/newcomputermodern]

Needs fontTools and brotli.
"""
import pathlib
import shutil
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

SRC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else
                   '/usr/share/texlive/texmf-dist/fonts/opentype/public/newcomputermodern')
LICENSE = pathlib.Path('/usr/share/texlive/texmf-dist/doc/fonts/newcomputermodern/License.txt')
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'static/fonts/newcm'
SCSS = ROOT / 'assets/scss/_fonts.scss'
URL = '/fonts/newcm/'

# NewCM's "Regular" is Knuth's original hairline weight; "Book" is the
# slightly heavier cut meant for reading, so Book is CSS 400 and Regular 300.
TEXT = {
    'NewCM Sans': [
        ('NewCMSans10-Regular.otf', 300, 'normal', 'sans-regular'),
        ('NewCMSans10-Oblique.otf', 300, 'italic', 'sans-oblique'),
        ('NewCMSans10-Book.otf', 400, 'normal', 'sans-book'),
        ('NewCMSans10-BookOblique.otf', 400, 'italic', 'sans-book-oblique'),
        ('NewCMSans10-Bold.otf', 700, 'normal', 'sans-bold'),
        ('NewCMSans10-BoldOblique.otf', 700, 'italic', 'sans-bold-oblique'),
    ],
    'NewCM Mono': [
        ('NewCMMono10-Regular.otf', 300, 'normal', 'mono-regular'),
        ('NewCMMono10-Italic.otf', 300, 'italic', 'mono-italic'),
        ('NewCMMono10-Book.otf', 400, 'normal', 'mono-book'),
        ('NewCMMono10-BookItalic.otf', 400, 'italic', 'mono-book-italic'),
        ('NewCMMono10-Bold.otf', 700, 'normal', 'mono-bold'),
        ('NewCMMono10-BoldOblique.otf', 700, 'italic', 'mono-bold-oblique'),
    ],
    'NewCM Serif': [
        ('NewCM10-Regular.otf', 300, 'normal', 'serif-regular'),
        ('NewCM10-Italic.otf', 300, 'italic', 'serif-italic'),
        ('NewCM10-Book.otf', 400, 'normal', 'serif-book'),
        ('NewCM10-BookItalic.otf', 400, 'italic', 'serif-book-italic'),
        ('NewCM10-Bold.otf', 700, 'normal', 'serif-bold'),
        ('NewCM10-BoldItalic.otf', 700, 'italic', 'serif-bold-italic'),
    ],
}
MATH = {
    'NewCM Sans Math': [('NewCMSansMath-Regular.otf', 400, 'normal', 'sans-math')],
    'NewCM Math': [
        ('NewCMMath-Regular.otf', 300, 'normal', 'math-regular'),
        ('NewCMMath-Book.otf', 400, 'normal', 'math-book'),
        ('NewCMMath-Bold.otf', 700, 'normal', 'math-bold'),
    ],
}

# Script subsets, the same split Google Fonts uses. Ukrainian needs latin
# (punctuation: « » — ’) plus cyrillic (including Ґґ).
RANGES = {
    'latin': 'U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, '
             'U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD',
    'latin-ext': 'U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+1D00-1DBF, U+1E00-1E9F, '
                 'U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF',
    'cyrillic': 'U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116',
    'cyrillic-ext': 'U+0460-048F, U+0492-04AF, U+04B2-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F',
    'greek': 'U+0370-0377, U+037A-037F, U+0384-038A, U+038C, U+038E-03A1, U+03A3-03FF',
    'greek-ext': 'U+1F00-1FFF',
}


def parse(ranges):
    out = set()
    for part in ranges.split(','):
        a, _, b = part.strip()[2:].partition('-')
        out.update(range(int(a, 16), int(b or a, 16) + 1))
    return out


def as_range(codes):
    """Compress codepoints into a unicode-range value."""
    codes, parts, i = sorted(codes), [], 0
    while i < len(codes):
        j = i
        while j + 1 < len(codes) and codes[j + 1] == codes[j] + 1:
            j += 1
        parts.append(f'U+{codes[i]:04X}' + (f'-{codes[j]:04X}' if j > i else ''))
        i = j + 1
    return ', '.join(parts)


def options():
    o = subset.Options()
    o.flavor = 'woff2'
    o.layout_features = ['*']
    o.name_IDs = ['*']
    o.name_languages = ['*']
    o.notdef_outline = True
    o.glyph_names = False
    return o


def face(family, weight, style, src, unicode_range=None):
    rule = (f'@font-face {{\n  font-family: "{family}";\n  font-style: {style};\n  font-weight: {weight};\n'
            f'  font-display: swap;\n  src: url("{URL}{src}") format("woff2");\n')
    if unicode_range:
        rule += f'  unicode-range: {unicode_range};\n'
    return rule + '}\n'


def fallback_metrics():
    """Metric overrides that make local Arial take up the same room as
    NewCM Sans Book, so text doesn't jump when the web font arrives."""
    newcm = TTFont(SRC / 'NewCMSans10-Book.otf')
    arial_path = next((p for p in [pathlib.Path('/usr/share/fonts/ms-core/Arial.ttf'),
                                   pathlib.Path('/usr/share/fonts/liberation-sans-fonts/LiberationSans-Regular.ttf')]
                       if p.exists()), None)
    if not arial_path:
        return None
    arial = TTFont(arial_path)
    # Width of a typical lowercase run, weighted roughly by letter frequency.
    sample = 'eeeeeeeeeeeettttttttaaaaaaaoooooooiiiiiiinnnnnnsssssshhhhhhrrrrrdddddlllluuuccmmwwffggyyppbbvk  '

    def width(font):
        cmap, hmtx = font.getBestCmap(), font['hmtx']
        return sum(hmtx[cmap[ord(c)]][0] for c in sample) / font['head'].unitsPerEm

    adjust = width(newcm) / width(arial)
    upem, hhea = newcm['head'].unitsPerEm, newcm['hhea']
    return dict(size=adjust, ascent=hhea.ascent / upem / adjust,
                descent=-hhea.descent / upem / adjust, gap=hhea.lineGap / upem / adjust)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    rules, total = [], 0
    named = set().union(*(parse(r) for r in RANGES.values()))

    for family, faces in TEXT.items():
        rules.append(f'// {family}\n')
        for fname, weight, style, slug in faces:
            font_codes = set(TTFont(SRC / fname).getBestCmap())
            pieces = {name: parse(r) & font_codes for name, r in RANGES.items()}
            pieces['symbols'] = font_codes - named
            for name, codes in pieces.items():
                if not codes:
                    continue
                font = TTFont(SRC / fname)
                sub = subset.Subsetter(options())
                sub.populate(unicodes=codes)
                sub.subset(font)
                out = f'{slug}-{name}.woff2'
                font.flavor = 'woff2'
                font.save(OUT / out)
                total += (OUT / out).stat().st_size
                rules.append(face(family, weight, style, out, RANGES.get(name) or as_range(codes)))

    for family, faces in MATH.items():
        rules.append(f'// {family}: whole font, the MATH table needs every glyph\n')
        for fname, weight, style, slug in faces:
            font = TTFont(SRC / fname)
            font.flavor = 'woff2'
            out = f'{slug}.woff2'
            font.save(OUT / out)
            total += (OUT / out).stat().st_size
            rules.append(face(family, weight, style, out))

    fb = fallback_metrics()
    if fb:
        rules.append('// Local Arial resized to NewCM Sans metrics, shown until the web font loads\n')
        rules.append('@font-face {\n  font-family: "NewCM Sans Fallback";\n'
                     '  src: local("Arial"), local("ArialMT"), local("Liberation Sans"), local("Helvetica");\n'
                     f'  size-adjust: {fb["size"] * 100:.2f}%;\n  ascent-override: {fb["ascent"] * 100:.2f}%;\n'
                     f'  descent-override: {fb["descent"] * 100:.2f}%;\n  line-gap-override: {fb["gap"] * 100:.2f}%;\n}}\n')

    if LICENSE.exists():
        shutil.copy(LICENSE, OUT / 'LICENSE.txt')
    header = ('// New Computer Modern web fonts. Generated by tools/build-fonts.py; do not edit.\n'
              '// Fonts by Antonis Tsolomitis, GUST Font License / GPL3+FE (see static/fonts/newcm/LICENSE.txt).\n\n')
    SCSS.write_text(header + '\n'.join(rules))
    files = len(list(OUT.glob('*.woff2')))
    print(f'{files} files, {total / 1024 / 1024:.1f} MB in {OUT.relative_to(ROOT)}; rules in {SCSS.relative_to(ROOT)}')
    if fb:
        print('fallback: ' + ', '.join(f'{k} {v * 100:.1f}%' for k, v in fb.items()))


main()
