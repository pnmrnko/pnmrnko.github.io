---
title: "OpenStreetMap у коді"
slug: osm-u-kodi
date: 2026-10-08T16:20:00+03:00
toc: true
---

Після формул настала черга коду. Блок коду в дописі — це три зворотні лапки й назва мови, а решту робить збірка сайту: Hugo розфарбовує код ще до публікації, тож у браузері лише готовий HTML. Вбудований підсвічувач Chroma знає близько 250 мов, а мови, яких він не знає, можна описати самому.

Щоб перевірити все в ділі, ось одна мапова задача від формули до правки.

## Відстань між двома точками

Відстань по поверхні Землі між точками $(\varphi_1, \lambda_1)$ і $(\varphi_2, \lambda_2)$ дає формула гаверсинусів:

$$
d = 2R \arcsin\sqrt{\sin^2\frac{\varphi_2 - \varphi_1}{2} + \cos\varphi_1 \cos\varphi_2 \sin^2\frac{\lambda_2 - \lambda_1}{2}}
$$

У LaTeX вона записана так:

```latex
d = 2R \arcsin\sqrt{\sin^2\frac{\varphi_2 - \varphi_1}{2}
  + \cos\varphi_1 \cos\varphi_2 \sin^2\frac{\lambda_2 - \lambda_1}{2}}
```

А ось вона ж кількома мовами. Від Києва до Львова виходить 467,5 км. Python, де жовтим виділено саму формулу (`hl_lines`):

```python {hl_lines="9-10"}
from math import asin, cos, radians, sin, sqrt

EARTH_RADIUS_KM = 6371.0


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Відстань по дузі великого кола, км."""
    φ1, φ2 = radians(lat1), radians(lat2)
    h = (sin((φ2 - φ1) / 2) ** 2
         + cos(φ1) * cos(φ2) * sin(radians(lon2 - lon1) / 2) ** 2)
    return 2 * EARTH_RADIUS_KM * asin(sqrt(h))


print(f"{haversine(50.4501, 30.5234, 49.8397, 24.0297):.1f} км")  # 467.5 км
```

Go, з номерами рядків (`linenos`):

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

А в базі з PostGIS рахувати нічого не треба:

```sql
SELECT round(ST_Distance(
         'SRID=4326;POINT(30.5234 50.4501)'::geography,
         'SRID=4326;POINT(24.0297 49.8397)'::geography
       ) / 1000) AS km;  -- 467: PostGIS рахує на еліпсоїді, а не на кулі
```

## Запит до Overpass

Тепер знайдімо на мапі кафе біля Хрещатику. Для цього є Overpass API і його мова запитів Overpass QL. Chroma її не знає, тож правила підсвітки описано в `data/syntax/overpassql.yaml`:

```overpassql
/* Кафе й ресторани в радіусі 300 м від Майдану Незалежності */
[out:json][timeout:25];

nwr(around:300, 50.4501, 30.5234)[amenity~"^(cafe|restaurant)$"]->.food;
.food out center tags;

(.food; - nwr.food["opening_hours"];)->.noHours;
.noHours out count;  // скільки з них без годин роботи
```

У overpass turbo замість координат можна писати `{{bbox}}` — це межі видимої частини мапи:

```overpass
[out:xml][bbox:{{bbox}}];
nwr[amenity=cafe][!wheelchair];
out meta;
```

Запит можна відправити і з терміналу:

```bash
#!/usr/bin/env bash
set -euo pipefail

query='[out:json];node(around:300,50.4501,30.5234)[amenity=cafe];out;'
curl --silent --data-urlencode "data=${query}" \
  https://overpass-api.de/api/interpreter |
  jq -r '.elements[] | "\(.id)\t\(.tags.name // "—")"'
```

Ось як це виглядає в терміналі (`console`, де запрошення й вивід розфарбовані по-різному):

```console
$ ./cafes.sh | head -3
4294967296	Kyiv Coffee
240109189	—
1500000001	Під каштанами
$ echo $?
0
```

А сам Overpass відповідає таким JSON:

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

## Правка в Level0L

Level0 — вебредактор OpenStreetMap, де об’єкти правлять як текст. Його формат називається Level0L; для нього є розширення VS Code, а тепер і підсвітка тут (`data/syntax/level0l.yaml`). Номери рядків і виділення для таких мов теж працюють, тут виділено змінені й нові рядки:

```l0l {linenos=table hl_lines="8-9 11-14"}
changeset
  comment = Хрещатик: години роботи кафе й нова лавка
  source = survey

node 4294967296.3: 50.4501, 30.5234
  amenity = cafe
  name = Kyiv Coffee
  opening_hours = Mo-Fr 08:00-20:00; Sa 09:00-18:00
  wheelchair = yes

# Нова лавка: від’ємний id, координати обов’язкові
node -1: 50.4502, 30.5240
  amenity = bench
  backrest = yes

way 123456789.7
  nd 4294967296
  nd -1
  highway = footway

-node 1500000003.2: 50.4509, 30.5230
```

Що саме змінилося, видно з диффу:

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

## Як додати свою мову

Опис мови — це YAML-файл у `data/syntax/` зі списком регулярних виразів. Перший вираз, що підійшов, визначає клас токена, а класи ті самі, що в Chroma, тож кольори беруться зі спільної теми. Ось шматок опису Overpass QL:

```yaml
name: Overpass QL
aliases: [overpass, oql]

tokens:
  main:
    - {re: '//[^\n]*', class: c1}                # коментар
    - {re: '"(?:[^"\\\n]|\\.)*"', class: s2}     # рядок
    - {re: '\b(?:node|way|rel|nwr|area)\b', class: kt}
    - {re: '\.[A-Za-z_][A-Za-z0-9_]*', class: nv} # множина: .food
```

Мову для Hugo вмикає сам шаблон: якщо Chroma мову знає, блок іде йому, а якщо для неї є файл у `data/syntax/`, шаблон розбирає код сам.

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

А налаштування Hugo, від яких усе це залежить, лежать у `hugo.toml`:

```toml
[markup.highlight]
  noClasses = false   # класи замість вбудованих стилів: тема в CSS

[markup.goldmark.extensions.passthrough]
  enable = true       # формули LaTeX — з попереднього допису
```

## Кунсткамера

Наостанок — «Привіт, мапо!» мовами, далекими від OpenStreetMap, які Chroma однаково розфарбує. Підсвітку можна вмикати й посеред рядка: {{< highlight go "hl_inline=true" >}}fmt.Println("Привіт, мапо!"){{< /highlight >}}.

Fortran:

```fortran
program hello
  print *, "Привіт, мапо!"
end program hello
```

COBOL:

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.
       PROCEDURE DIVISION.
           DISPLAY "Привіт, мапо!".
           STOP RUN.
```

Ada:

```ada
with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
   Put_Line ("Привіт, мапо!");
end Hello;
```

Prolog:

```prolog
:- initialization(main).
main :- format("Привіт, мапо!~n"), halt.
```

Erlang:

```erlang
-module(hello).
-export([main/0]).
main() -> io:format("Привіт, мапо!~n").
```

Elixir:

```elixir
defmodule Hello do
  def main, do: IO.puts("Привіт, мапо!")
end
```

Clojure:

```clojure
(ns hello.core)
(defn -main [] (println "Привіт, мапо!"))
```

Zig:

```zig
const std = @import("std");
pub fn main() void {
    std.debug.print("Привіт, мапо!\n", .{});
}
```

Julia:

```julia
println("Привіт, мапо!")
```

Lua:

```lua
print("Привіт, мапо!")
```

PowerShell:

```powershell
Write-Host "Привіт, мапо!" -ForegroundColor Green
```

Асемблер x86-64 (NASM):

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
// Шейдер, що малює мапу «у клітинку»
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

Остання — класична програма на Brainfuck, що друкує «Hello World!».
