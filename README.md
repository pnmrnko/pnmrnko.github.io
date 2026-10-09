# pnmrnko.github.io

Особистий двомовний блог на [Hugo](https://gohugo.io/) з темою
[Poole](https://github.com/poole/poole) від @mdo, перенесеною з Jekyll.
Сайт: https://pnmrnko.github.io/

## Робота локально

```sh
hugo server -D -M     # http://localhost:1313, з чернетками, у памʼяті
hugo --gc --minify    # збірка в public/
```

Потрібен Hugo extended (версія — у `.github/workflows/hugo.yml`).

## Мови

Українська — основна, на корені сайту; англійська — під `/en/`.
Переклад лежить поруч з оригіналом і має те саме імʼя з іншим суфіксом:

```
content/posts/2026-10-pershyi-dopys/index.uk.md   → /2026/10/pershyi-dopys/
content/posts/2026-10-pershyi-dopys/index.en.md   → /en/2026/10/first-post/
```

- `slug` у кожній мові свій, латиницею.
- Допис без перекладу показується лише у своїй мові; перемикач мов тоді веде
  на головну іншої мови.
- Написи інтерфейсу — у `i18n/uk.yaml` та `i18n/en.yaml`.

## Новий допис

```sh
hugo new content posts/2026-11-nazva/index.uk.md
```

У front matter: `title`, `slug`, `date`. Поки стоїть `draft: true`, допис не
публікується. На головній дописи показуються повністю, без «Читати далі».
`toc: true` додає зміст.

## Фото й відео

```
{{< photo src="P1110004.jpg" caption="Підпис" >}}
{{< embed provider="youtube" id="YH3c1QZzRK4" title="Назва" >}}
{{< embed provider="spotify" id="2xWVD6aecDSHroyPVVcPpa" title="Виконавець — Трек" >}}
{{< embed provider="soundcloud" id="396827769" title="Виконавець — Трек" >}}
{{< embed provider="bandcamp" id="3216491533" title="Виконавець — Трек" >}}
```

Фото лежить у теці допису поруч з `index.uk.md`; поки файлу немає, шорткод
нічого не показує. Великі фото зменшуються до 1440 px у WebP. Для схем із
дрібним текстом — `link="true"`: клік відкриває оригінал повного розміру.

Таблиця, ширша за колонку, гортається вбік сама (пальцем на телефоні),
не розширюючи сторінку: `layouts/_markup/render-table.html`.

Апостроф в українському тексті — ʼ (U+02BC): обʼєкт, пʼять.
Для широкоформатного відео додайте `ratio="40/17"` (або `"2.35"`) — тоді
плеєр матиме форму кадру без чорних смуг. Це працює, лише якщо смуги додає
плеєр, а не вшиті у файл; перевірити можна за розміром сторіборду:
`yt-dlp --extractor-args youtube:player_client=web_embedded -F <url>`
(рядок `sb0`, наприклад 105×45 — це 2,35:1, а 160×90 — 16:9).

`embed` уміє `youtube`, `vimeo`, `coub`, `spotify`, `soundcloud`, `bandcamp`;
для відео, яке власник не дозволяє вбудовувати, додайте `link="true"` — буде
картка-посилання. Для музики краще знайти трек на Spotify: `id` — частина
посилання після `open.spotify.com/track/` (без `?si=…`). Без входу в Spotify
плеєр грає 30-секундний уривок; SoundCloud і Bandcamp грають повністю всім.
У SoundCloud `id` — числовий ID треку з коду вставки (`tracks/…`), у Bandcamp —
з `EmbeddedPlayer/track=…` у «Share / Embed».

Короткий беззвучний кліп замість GIF — `{{< loop name="назва" title="…" >}}`;
поруч із дописом мають лежати `назва.webm` (AV1), `назва.mp4` (H.264) і
`назва.jpg` (перший кадр). Наприклад:

```sh
ffmpeg -ss 2.56 -i src.mp4 -frames:v 64 -an -c:v libsvtav1 -crf 36 -preset 4 -g 64 назва.webm
ffmpeg -ss 2.56 -i src.mp4 -frames:v 64 -an -c:v libx264 -crf 24 -preset veryslow \
  -profile:v high -level:v 3.1 -pix_fmt yuv420p -movflags +faststart назва.mp4
ffmpeg -ss 2.56 -i src.mp4 -frames:v 1 -q:v 2 назва.jpg
```

## Шрифти

Увесь сайт набрано New Computer Modern: текст — New CM Sans, код — New CM
Mono, формули — New CM Sans Math. WOFF2-файли лежать у `static/fonts/newcm/`,
правила `@font-face` — в `assets/scss/_fonts.scss`; і те, й інше генерує

```sh
python3 tools/build-fonts.py   # з TeX Live; потрібні fontTools і brotli
```

Текстові накреслення порізано за письменами (латиниця, кирилиця, грецька…),
тож сторінка завантажує лише те, що на ній є. Доступні також New CM Serif і
New CM Math, якщо колись знадобляться. Ліцензії — `static/fonts/newcm/LICENSE.txt`.

## Формули

LaTeX між `$…$` або `\(…\)` — у рядку, між `$$…$$` або `\[…\]` — окремим
блоком. Hugo перетворює його на MathML ще під час збірки, тож на сторінках
немає JavaScript; браузер малює формули шрифтом New CM Sans Math. Помилка
в формулі зупиняє збірку й називає файл. Приклади — у чернетці
`content/typography.uk.md` (`hugo server -D -M`, сторінка `/typography/`)
і в дописі «Космос у формулах» (`content/posts/2026-10-kosmos-u-formulakh/`),
де зібрано майже все, що вміє KaTeX: `aligned`, `gathered`, `cases`, матриці,
`array` з лініями, `\tag`, `\boxed`, `\cancel`, `\xrightarrow`, діаграми
`CD`, хімія `\ce{…}`, кольори.

Не працюють `multline`, `\label`/`\eqref` (номер посилання пишіть руками),
`\sideset`, `\href`, `\includegraphics`; кирилиця — лише в `\text{…}`.
`\mathsf` і `\mathtt` браузер малює чужим шрифтом: у New CM Sans Math немає
цих накреслень. Що Chrome у MathML від KaTeX малює неправильно (рамки,
закреслення, лінії таблиць, підписи стрілок, вирівнювання `aligned`, проміжки
біля `\cos`), латає `layouts/_markup/render-passthrough.html` разом зі
стилями в `assets/scss/_site.scss`.

## Код

Після трьох зворотних лапок — назва мови; Hugo розфарбовує код під час
збірки (Chroma, ~250 мов, кольори — `assets/scss/_syntax.scss`). Атрибути
блоку: `{linenos=table hl_lines="2 4-5" linenostart=10}`. У рядку —
`{{< highlight go "hl_inline=true" >}}fmt.Println(1){{< /highlight >}}`.

Мови, яких Chroma не знає, описано в `data/syntax/<назва>.yaml`: зараз це
Overpass QL (`overpassql`, `overpass`, `oql`) і Level0L (`l0l`, `level0`,
`level0l`, за граматикою з pnmrnko/level0-vscode). Опис — регулярні вирази з
класами Chroma: `tokens` (перший збіг виграє) і, за потреби, `lines` —
правила на цілий рядок, групи яких розфарбовуються окремо. Розбирає їх
`layouts/_markup/render-codeblock.html`; `linenos` і `hl_lines` працюють і
для них. Новій мові досить нового YAML-файлу. Приклади — у дописі
«OpenStreetMap у коді» (`content/posts/2026-10-osm-u-kodi/`).

## Коментарі

Під кожним дописом — [giscus](https://giscus.app): коментарі зберігаються
в GitHub Discussions цього репозиторію (категорія «Announcements»), для
коментування потрібен акаунт GitHub. Віджет вантажиться, лише коли читач
догортає до нього, мова — за мовою сторінки, тема — за системною.
Набрано його шрифтами й кольорами сайту: тема `assets/scss/giscus.scss` бере
світлу чи темну тему giscus і підміняє в ній шрифти та кольори (змінні Primer —
на сірі, синій і кольори коду з `_variables.scss` і `_syntax.scss`, для обох
тем); giscus вантажить її з сайту за
повною адресою (тому локально, з `hugo server`, тема не застосовується —
giscus.app не отримує дозволу CORS, а GitHub Pages його дає).
Налаштування — `[params.giscus]` у `hugo.toml`, розмітка —
`layouts/_partials/comments.html`. Щоб вимкнути коментарі під дописом,
додайте `comments: false` у front matter.

## Старий блог

Дописи 2006–2018 перенесено з Aegea (pnmrnko.pp.ua). Фото з нього не
збереглися: у дописах лишилися шорткоди `photo` з іменами файлів, тож
знайдені фото достатньо покласти в теку допису. Дописи, які без фото
чи через видалене відео не мають сенсу, стоять як `draft: true`.

## Публікація

Кожен push у `main` збирає й публікує сайт через GitHub Actions
(Settings → Pages → Source: GitHub Actions).

## Сторінки rclone

`/rclone-google-drive/` і `/rclone-google-drive/privacy.html` — домашня
сторінка й політика приватності OAuth-клієнта Google. Ці адреси вписані
в налаштування Google Cloud, тож їх не можна змінювати
(`url` у front matter).

## Ліцензії

Стилі теми — Poole © Mark Otto, MIT (`assets/scss/LICENSE-poole.md`).
