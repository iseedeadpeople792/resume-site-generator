# resume-site-generator

Генератор одностраничного резюме-сайта из JSON-файла. Python без зависимостей, на выходе один HTML с тёмной и светлой темой.

## Запуск
```
cp data.example.json data.json   # впишите свои данные
python build.py data.json index.html
```
Готовый `index.html` можно выложить на GitHub Pages.

## Формат данных
`name`, `role`, `about`, `skills` (список), `jobs` (список объектов `title`, `company`, `years`, `text`), `contacts` (словарь «название → ссылка»).

Весь пользовательский текст экранируется, поэтому HTML-код в данных не сломает страницу.

## Тесты
```
python -m unittest -v
```

Учебный проект для портфолио. Python 3.9+.
