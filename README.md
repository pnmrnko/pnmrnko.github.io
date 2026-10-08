# pnmrnko.github.io

Особистий двомовний блог на [Hugo](https://gohugo.io/) з темою
[Poole](https://github.com/poole/poole) від @mdo, перенесеною з Jekyll.
Сайт: https://pnmrnko.github.io/

## Робота локально

```sh
hugo server -D        # http://localhost:1313, разом із чернетками
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
публікується. Щоб на головній показувався лише початок, поставте `<!--more-->`
після вступу. `toc: true` додає зміст.

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
