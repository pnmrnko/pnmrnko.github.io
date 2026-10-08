# pnmrnko.github.io

Особистий двомовний блог на [Hugo](https://gohugo.io/) з темою
[Poole](https://github.com/poole/poole) від @mdo, перенесеною з Jekyll.
Сайт: https://pnmrnko.github.io/

## Робота локально

```sh
hugo server -D -M     # http://localhost:1313, з чернетками, у пам’яті
hugo --gc --minify    # збірка в public/
```

Потрібен Hugo extended (версія — у `.github/workflows/hugo.yml`).

## Мови

Українська — основна, на корені сайту; англійська — під `/en/`.
Переклад лежить поруч з оригіналом і має те саме ім’я з іншим суфіксом:

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
```

Фото лежить у теці допису поруч з `index.uk.md`; поки файлу немає, шорткод
нічого не показує. Великі фото зменшуються до 1440 px у WebP.
`embed` уміє `youtube`, `vimeo`, `coub`, `soundcloud`; для відео, яке власник
не дозволяє вбудовувати, додайте `link="true"` — буде картка-посилання.

Короткий беззвучний кліп замість GIF — `{{< loop name="назва" title="…" >}}`;
поруч із дописом мають лежати `назва.webm` (AV1), `назва.mp4` (H.264) і
`назва.jpg` (перший кадр). Наприклад:

```sh
ffmpeg -ss 2.56 -i src.mp4 -frames:v 64 -an -c:v libsvtav1 -crf 36 -preset 4 -g 64 назва.webm
ffmpeg -ss 2.56 -i src.mp4 -frames:v 64 -an -c:v libx264 -crf 24 -preset veryslow \
  -profile:v high -level:v 3.1 -pix_fmt yuv420p -movflags +faststart назва.mp4
ffmpeg -ss 2.56 -i src.mp4 -frames:v 1 -q:v 2 назва.jpg
```

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
