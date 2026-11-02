# Код безопасности — интерактивный кроссворд

Учебная игра по производственной безопасности: 4 уровня, 40 слов. Один автономный файл `index.html`
(шрифт и логотип встроены), без сервера и внешних запросов. Прогресс хранится в браузере игрока.

## Публикация на GitHub Pages
1. Создать репозиторий (например, `kod-bezopasnosti`) и загрузить файлы этой папки.
2. Settings → Pages → Source: **Deploy from a branch**, Branch: **main**, папка **/ (root)** → Save.
3. Через 1–2 минуты игра доступна по адресу `https://<логин>.github.io/kod-bezopasnosti/`.

## QR-код и плакат
```
pip install segno pillow
python3 tools/make_qr.py https://<логин>.github.io/kod-bezopasnosti/
```
Результат в `qr/`: `qr.svg` (вектор для типографии), `qr.png`, `poster_a4.png` (A4, 300 dpi).

## Обновление игры
Исходники и сборка — в проекте `crossword_prod` (`build/build.py`); собранный `dist/kod_bezopasnosti.html` копируется сюда как `index.html`.
