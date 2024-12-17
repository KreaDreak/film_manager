# Фильм менеджер

Приложение для управления библиотекой фильмов

## Оглавление
- [Требования](#требования)
- [Установка](#установка)
- [Использование](#использование)


---

## Требования
Для запуска приложения требуется:
- Python 3.7+


---

## Установка
1. Склонируйте репозиторий или загрузите файлы проекта.
2. Убедитесь, что у вас есть файл `films_db.json` в корневой папке с содержимым следующего вида:
```json
[
  {
    "title": "Star Wars: Episode III — Revenge of the Sith",
    "genre": "Epic Space Opera",
    "year": 2005,
    "rating": 8.1
  },
  {
    "title": "Attack on Titan",
    "genre": "Action",
    "year": 2013,
    "rating": 8.7
  }
]
```
3. Запустите приложение: ```python3 main.py```


## Использование
1. **Список фильмов**: выберите "Вывести список фильмов" чтобы увидеть список доступных фильмов.
2. **Добавить фильм**: выберите "Добавить фильм" и введите нужную информацию
3. **Удаление фильма**: выберите "Удалить фильм" и введите название фильма
4. **Поиск по жанру**: выберите "Поиск по жанру" и введите желаемый жанр
5. **Поиск по рейтингу**: выберите "Поиск по рейтингу" и введите желаемый рейтинг
6. **Сохранение изменений**: выберите "Выйти", чтобы сохранить изменения
