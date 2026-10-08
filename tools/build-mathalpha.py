#!/usr/bin/env python3
"""Write data/mathalpha.json: for each MathML mathvariant, a map from plain
letters and digits to their Unicode Mathematical Alphanumeric Symbols.

Chrome follows MathML Core, which ignores mathvariant other than "normal";
the passthrough render hook uses this table to swap <mi mathvariant="double-struck">R</mi>
for <mi>ℝ</mi>, which every browser draws from the math font.
"""
import json
import pathlib
import string
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent

# mathvariant → Unicode name prefix (KaTeX uses MathML's spelling, e.g. bold-sans-serif)
VARIANTS = {
    'bold': 'BOLD', 'italic': 'ITALIC', 'bold-italic': 'BOLD ITALIC',
    'double-struck': 'DOUBLE-STRUCK', 'script': 'SCRIPT', 'bold-script': 'BOLD SCRIPT',
    'fraktur': 'FRAKTUR', 'bold-fraktur': 'BOLD FRAKTUR',
    'sans-serif': 'SANS-SERIF', 'bold-sans-serif': 'SANS-SERIF BOLD',
    'sans-serif-italic': 'SANS-SERIF ITALIC', 'sans-serif-bold-italic': 'SANS-SERIF BOLD ITALIC',
    'monospace': 'MONOSPACE',
}
# Letters that live in Letterlike Symbols instead of the math block (the "holes").
HOLES = {
    'ITALIC SMALL H': 'PLANCK CONSTANT',
    'SCRIPT CAPITAL B': 'SCRIPT CAPITAL B', 'SCRIPT CAPITAL E': 'SCRIPT CAPITAL E',
    'SCRIPT CAPITAL F': 'SCRIPT CAPITAL F', 'SCRIPT CAPITAL H': 'SCRIPT CAPITAL H',
    'SCRIPT CAPITAL I': 'SCRIPT CAPITAL I', 'SCRIPT CAPITAL L': 'SCRIPT CAPITAL L',
    'SCRIPT CAPITAL M': 'SCRIPT CAPITAL M', 'SCRIPT CAPITAL R': 'SCRIPT CAPITAL R',
    'SCRIPT SMALL E': 'SCRIPT SMALL E', 'SCRIPT SMALL G': 'SCRIPT SMALL G', 'SCRIPT SMALL O': 'SCRIPT SMALL O',
    'FRAKTUR CAPITAL C': 'BLACK-LETTER CAPITAL C', 'FRAKTUR CAPITAL H': 'BLACK-LETTER CAPITAL H',
    'FRAKTUR CAPITAL I': 'BLACK-LETTER CAPITAL I', 'FRAKTUR CAPITAL R': 'BLACK-LETTER CAPITAL R',
    'FRAKTUR CAPITAL Z': 'BLACK-LETTER CAPITAL Z',
    'DOUBLE-STRUCK CAPITAL C': 'DOUBLE-STRUCK CAPITAL C', 'DOUBLE-STRUCK CAPITAL H': 'DOUBLE-STRUCK CAPITAL H',
    'DOUBLE-STRUCK CAPITAL N': 'DOUBLE-STRUCK CAPITAL N', 'DOUBLE-STRUCK CAPITAL P': 'DOUBLE-STRUCK CAPITAL P',
    'DOUBLE-STRUCK CAPITAL Q': 'DOUBLE-STRUCK CAPITAL Q', 'DOUBLE-STRUCK CAPITAL R': 'DOUBLE-STRUCK CAPITAL R',
    'DOUBLE-STRUCK CAPITAL Z': 'DOUBLE-STRUCK CAPITAL Z',
}
DIGITS = 'ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE'.split()
GREEK = {unicodedata.lookup(f'GREEK {case} LETTER {n}'): f'{case} {n}'
         for case in ('CAPITAL', 'SMALL')
         for n in 'ALPHA BETA GAMMA DELTA EPSILON ZETA ETA THETA IOTA KAPPA LAMDA MU NU XI OMICRON PI RHO SIGMA TAU UPSILON PHI CHI PSI OMEGA'.split()}


def lookup(prefix, tail):
    key = f'{prefix} {tail}'
    try:
        return unicodedata.lookup(HOLES.get(key) or f'MATHEMATICAL {key}')
    except KeyError:
        return None


table = {}
for variant, prefix in VARIANTS.items():
    m = {}
    for c in string.ascii_uppercase:
        m[c] = lookup(prefix, f'CAPITAL {c}')
    for c in string.ascii_lowercase:
        m[c] = lookup(prefix, f'SMALL {c.upper()}')
    for d, name in zip(string.digits, DIGITS):
        m[d] = lookup(prefix, f'DIGIT {name}')
    for ch, name in GREEK.items():
        m[ch] = lookup(prefix, name.replace('LAMDA', 'LAMDA'))
    table[variant] = {k: v for k, v in m.items() if v}

out = ROOT / 'data/mathalpha.json'
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(table, ensure_ascii=False, indent=1, sort_keys=True) + '\n')
print({k: len(v) for k, v in table.items()})
