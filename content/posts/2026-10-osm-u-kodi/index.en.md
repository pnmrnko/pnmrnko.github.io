---
title: "OpenStreetMap in Code"
slug: osm-in-code
date: 2026-10-08T16:20:00+03:00
toc: true
---

After formulas, it’s code’s turn. A code block in a post is three backticks and the name of a language, and the site build does the rest: Hugo colours the code before publishing, so the browser only gets finished HTML. Its built-in highlighter, Chroma, knows about 250 languages, and the ones it doesn’t know can be described by hand. That’s how Overpass QL and Level0L got here, the languages I edit OpenStreetMap with every day.

To put it through its paces, I’ll take one map task from a formula to an edit.

## Distance between two points

The distance over the Earth’s surface between points $(\varphi_1, \lambda_1)$ and $(\varphi_2, \lambda_2)$ is given by the haversine formula:

$$
d = 2R \arcsin\sqrt{\sin^2\frac{\varphi_2 - \varphi_1}{2} + \cos\varphi_1 \cos\varphi_2 \sin^2\frac{\lambda_2 - \lambda_1}{2}}
$$

In LaTeX it’s written like this:

```latex
d = 2R \arcsin\sqrt{\sin^2\frac{\varphi_2 - \varphi_1}{2}
  + \cos\varphi_1 \cos\varphi_2 \sin^2\frac{\lambda_2 - \lambda_1}{2}}
```

And here it is in several languages. From Kyiv to Lviv it comes to 467.5 km. Python, with the formula itself highlighted in yellow (`hl_lines`):

```python {hl_lines="9-10"}
from math import asin, cos, radians, sin, sqrt

EARTH_RADIUS_KM = 6371.0


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Great-circle distance, km."""
    φ1, φ2 = radians(lat1), radians(lat2)
    h = (sin((φ2 - φ1) / 2) ** 2
         + cos(φ1) * cos(φ2) * sin(radians(lon2 - lon1) / 2) ** 2)
    return 2 * EARTH_RADIUS_KM * asin(sqrt(h))


print(f"{haversine(50.4501, 30.5234, 49.8397, 24.0297):.1f} km")  # 467.5 km
```

Go, with line numbers (`linenos`):

```go {linenos=table}
package geo

import "math"

const earthRadiusKm = 6371.0

// Haversine returns the great-circle distance between two points, in km.
func Haversine(lat1, lon1, lat2, lon2 float64) float64 {
	rad := func(deg float64) float64 { return deg * math.Pi / 180 }
	dφ, dλ := rad(lat2-lat1), rad(lon2-lon1)
	h := math.Pow(math.Sin(dφ/2), 2) +
		math.Cos(rad(lat1))*math.Cos(rad(lat2))*math.Pow(math.Sin(dλ/2), 2)
	return 2 * earthRadiusKm * math.Asin(math.Sqrt(h))
}
```

Rust:

```rust
#[derive(Debug, Clone, Copy)]
pub struct Point {
    pub lat: f64,
    pub lon: f64,
}

impl Point {
    pub fn distance_km(self, other: Point) -> f64 {
        let (phi1, phi2) = (self.lat.to_radians(), other.lat.to_radians());
        let dlon = (other.lon - self.lon).to_radians();
        let h = ((phi2 - phi1) / 2.0).sin().powi(2)
            + phi1.cos() * phi2.cos() * (dlon / 2.0).sin().powi(2);
        2.0 * 6371.0 * h.sqrt().asin()
    }
}
```

C:

```c
#include <math.h>
#include <stdio.h>

#define EARTH_RADIUS_KM 6371.0
#define RAD(deg) ((deg) * M_PI / 180.0)

static double haversine(double lat1, double lon1, double lat2, double lon2)
{
    double h = pow(sin(RAD(lat2 - lat1) / 2), 2) +
               cos(RAD(lat1)) * cos(RAD(lat2)) * pow(sin(RAD(lon2 - lon1) / 2), 2);
    return 2 * EARTH_RADIUS_KM * asin(sqrt(h));
}

int main(void)
{
    printf("%.1f km\n", haversine(50.4501, 30.5234, 49.8397, 24.0297));
    return 0;
}
```

Haskell:

```haskell
haversine :: (Double, Double) -> (Double, Double) -> Double
haversine (lat1, lon1) (lat2, lon2) = 2 * r * asin (sqrt h)
  where
    r = 6371
    rad = (* (pi / 180))
    h = sin (rad (lat2 - lat1) / 2) ^ 2
      + cos (rad lat1) * cos (rad lat2) * sin (rad (lon2 - lon1) / 2) ^ 2
```

JavaScript:

```javascript
const rad = (deg) => (deg * Math.PI) / 180;

export function haversine([lat1, lon1], [lat2, lon2]) {
  const h =
    Math.sin(rad(lat2 - lat1) / 2) ** 2 +
    Math.cos(rad(lat1)) * Math.cos(rad(lat2)) * Math.sin(rad(lon2 - lon1) / 2) ** 2;
  return 2 * 6371 * Math.asin(Math.sqrt(h));
}

console.log(`${haversine([50.4501, 30.5234], [49.8397, 24.0297]).toFixed(1)} km`);
```

And in a PostGIS database there’s nothing to compute:

```sql
SELECT round(ST_Distance(
         'SRID=4326;POINT(30.5234 50.4501)'::geography,
         'SRID=4326;POINT(24.0297 49.8397)'::geography
       ) / 1000) AS km;  -- 467: PostGIS works on the ellipsoid, not a sphere
```

## An Overpass query

Now let’s find cafés near Khreshchatyk on the map. That’s what the Overpass API and its query language, Overpass QL, are for. Chroma doesn’t know it, so its highlighting rules are described in `data/syntax/overpassql.yaml`:

```overpassql
/* Cafés and restaurants within 300 m of Maidan Nezalezhnosti */
[out:json][timeout:25];

nwr(around:300, 50.4501, 30.5234)[amenity~"^(cafe|restaurant)$"]->.food;
.food out center tags;

(.food; - nwr.food["opening_hours"];)->.noHours;
.noHours out count;  // how many have no opening hours
```

In overpass turbo you can write `{{bbox}}` instead of coordinates, the bounds of the visible part of the map:

```overpass
[out:xml][bbox:{{bbox}}];
nwr[amenity=cafe][!wheelchair];
out meta;
```

The query can be sent from a terminal too:

```bash
#!/usr/bin/env bash
set -euo pipefail

query='[out:json];node(around:300,50.4501,30.5234)[amenity=cafe];out;'
curl --silent --data-urlencode "data=${query}" \
  https://overpass-api.de/api/interpreter |
  jq -r '.elements[] | "\(.id)\t\(.tags.name // "—")"'
```

Here’s how that looks in a terminal (`console`, where the prompt and the output get different colours):

```console
$ ./cafes.sh | head -3
4294967296	Kyiv Coffee
240109189	—
1500000001	Under the Chestnuts
$ echo $?
0
```

And Overpass itself answers with JSON like this:

```json
{
  "version": 0.6,
  "generator": "Overpass API 0.7.62",
  "elements": [
    {
      "type": "node",
      "id": 4294967296,
      "lat": 50.4501,
      "lon": 30.5234,
      "tags": { "amenity": "cafe", "name": "Kyiv Coffee", "wheelchair": "yes" }
    }
  ]
}
```

## An edit in Level0L

Level0 is an OpenStreetMap web editor where objects are edited as text. I call its format Level0L and have a VS Code extension for it, and now highlighting here too (`data/syntax/level0l.yaml`). Line numbers and highlighted lines work for these languages as well; here the changed and new lines are highlighted:

```l0l {linenos=table hl_lines="8-9 11-14"}
changeset
  comment = Khreshchatyk: cafe opening hours and a new bench
  source = survey

node 4294967296.3: 50.4501, 30.5234
  amenity = cafe
  name = Kyiv Coffee
  opening_hours = Mo-Fr 08:00-20:00; Sa 09:00-18:00
  wheelchair = yes

# A new bench: negative id, coordinates required
node -1: 50.4502, 30.5240
  amenity = bench
  backrest = yes

way 123456789.7
  nd 4294967296
  nd -1
  highway = footway

-node 1500000003.2: 50.4509, 30.5230
```

The diff shows exactly what changed:

```diff
--- a/khreshchatyk.l0l
+++ b/khreshchatyk.l0l
@@ -5,4 +5,5 @@
 node 4294967296.3: 50.4501, 30.5234
   amenity = cafe
   name = Kyiv Coffee
-  opening_hours = Mo-Fr 08:00-19:00
+  opening_hours = Mo-Fr 08:00-20:00; Sa 09:00-18:00
+  wheelchair = yes
```

## How to add a language

A language is a YAML file in `data/syntax/` with a list of regular expressions. The first one that matches decides the token’s class, and the classes are Chroma’s, so the colours come from the same theme. Here’s part of the Overpass QL description:

```yaml
name: Overpass QL
aliases: [overpass, oql]

tokens:
  main:
    - {re: '//[^\n]*', class: c1}                # comment
    - {re: '"(?:[^"\\\n]|\\.)*"', class: s2}     # string
    - {re: '\b(?:node|way|rel|nwr|area)\b', class: kt}
    - {re: '\.[A-Za-z_][A-Za-z0-9_]*', class: nv} # a set: .food
```

The template itself switches languages on: if Chroma knows the language, the block goes to it, and if there’s a file for it in `data/syntax/`, the template tokenizes the code itself.

```go-html-template
{{- $lang := lower .Type }}
{{- $def := false }}
{{- range $name, $d := hugo.Data.syntax }}
  {{- if or (eq $name $lang) (in ($d.aliases | default slice) $lang) }}
    {{- $def = $d }}
  {{- end }}
{{- end }}
{{- if not $def }}
  {{- (transform.HighlightCodeBlock .).Wrapped }}
{{- end }}
```

And the Hugo settings all of this depends on are in `hugo.toml`:

```toml
[markup.highlight]
  noClasses = false   # classes, not inline styles: the theme is CSS

[markup.goldmark.extensions.passthrough]
  enable = true       # LaTeX formulas, from the previous post
```

## A cabinet of curiosities

Finally, “Hello, map!” in languages I’ll probably never write for OpenStreetMap but Chroma colours all the same. Highlighting works in the middle of a sentence too: {{< highlight go "hl_inline=true" >}}fmt.Println("Hello, map!"){{< /highlight >}}.

Fortran:

```fortran
program hello
  print *, "Hello, map!"
end program hello
```

COBOL:

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.
       PROCEDURE DIVISION.
           DISPLAY "Hello, map!".
           STOP RUN.
```

Ada:

```ada
with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
   Put_Line ("Hello, map!");
end Hello;
```

Prolog:

```prolog
:- initialization(main).
main :- format("Hello, map!~n"), halt.
```

Erlang:

```erlang
-module(hello).
-export([main/0]).
main() -> io:format("Hello, map!~n").
```

Elixir:

```elixir
defmodule Hello do
  def main, do: IO.puts("Hello, map!")
end
```

Clojure:

```clojure
(ns hello.core)
(defn -main [] (println "Hello, map!"))
```

Zig:

```zig
const std = @import("std");
pub fn main() void {
    std.debug.print("Hello, map!\n", .{});
}
```

Julia:

```julia
println("Hello, map!")
```

Lua:

```lua
print("Hello, map!")
```

PowerShell:

```powershell
Write-Host "Hello, map!" -ForegroundColor Green
```

x86-64 assembly (NASM):

```nasm
section .data
    msg db "Hello, map!", 10
section .text
    global _start
_start:
    mov rax, 1          ; write
    mov rdi, 1          ; stdout
    mov rsi, msg
    mov rdx, 12
    syscall
    mov rax, 60         ; exit
    xor rdi, rdi
    syscall
```

GLSL:

```glsl
// A shader that draws a map grid
uniform vec2 resolution;
void main() {
    vec2 uv = gl_FragCoord.xy / resolution;
    float grid = step(0.98, fract(uv.x * 20.0)) + step(0.98, fract(uv.y * 20.0));
    gl_FragColor = vec4(vec3(1.0 - grid * 0.2), 1.0);
}
```

Brainfuck:

```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]
>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.
>>+.
```

The last one prints “Hello World!”: the classic program, nothing map-specific about it.
