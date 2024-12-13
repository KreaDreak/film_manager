import json


class FilmsManager:
    def __init__(self, db_path: str):
        self.films: list[dict] = []
        self.db_path = db_path
        self.load_db()

    def load_db(self) -> None:
        with open(self.db_path, 'r', encoding='utf-8') as f:
            self.films = json.load(f)

    def add_film(self, title: str, genre: str, year: int, rating: float) -> None:
        film = {
            "title": title,
            "genre": genre,
            "year": year,
            "rating": rating
        }
        self.films.append(film)

    def del_film(self, title: str) -> bool:
        for i, film in enumerate(self.films):
            if film['title'] == title:
                del self.films[i]
                return True
        return False

    def search_by_rating(self, rating: float):
        found_films = []
        for film in self.films:
            if film['rating'] >= rating:
                found_films.append(film)
        return found_films

    def search_by_genre(self, genre: str):
        found_films = []
        for film in self.films:
            if film['genre'].lower() == genre.lower():
                found_films.append(film)
        return found_films

    def save_db(self):
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(self.films, f, ensure_ascii=False)

    def __str__(self):
        films = ''
        for i, film in enumerate(self.films):
            films += f'{i + 1}. '
            for key, value in film.items():
                films += f'{key.title()}: {value}, '
            films += '\n'
        return films

    def manage(self):
        while True:
            print("Меню:")
            print("1. Добавить фильм")
            print("2. Удалить фильм")
            print("3. Поиск по рейтингу")
            print("4. Поиск по жанру")
            print("5. Вывести список фильмов")
            print("Q. Выход")

            user_input = input('Введите операцию: ').upper()

            if user_input == '1':
                title = input('Введите название фильма: ')
                genre = input('Введите жанр: ')
                try:
                    year = int(input('Введите год выпуска фильма: '))
                    rating = float(input('Введите рейтинг фильма: '))
                except ValueError:
                    print('Год или рейтинг должны быть числами')
                    continue
                self.add_film(title, genre, year, rating)
                print(f'Добавлен фильм {title}')
            elif user_input == '2':
                title = input('Введите название фильма, который хотите удалить: ')
                if self.del_film(title):
                    print(f'Фильм {title} удален!')
                else:
                    print(f'Фильм {title} не найден')
            elif user_input == '3':
                try:
                    rating = float(input('Введите рейтинг фильма: '))
                except ValueError:
                    print('Рейтинг должен быть дробным числом')
                    continue
                found_films = self.search_by_rating(rating)
                if found_films:
                    print(f'Фильмы с рейтингом {rating} и выше: ')
                    for i, film in enumerate(found_films):
                        print(f'{i + 1}. {film["title"]}, {film["rating"]}')
                else:
                    print(f'Фильмы с рейтингом {rating} не найдены')
            elif user_input == '4':
                genre = input('Введите жанр фильма: ')
                found_films = self.search_by_genre(genre)
                if found_films:
                    print(f'Фильмы жанра {genre}: ')
                    for i, film in enumerate(found_films):
                        print(f'{i + 1}. {film["title"]}')
                else:
                    print(f'Фильмы жанра {genre} не найдены')
            elif user_input == '5':
                    print(self)
            elif user_input == 'Q':
                    self.save_db()
                    print('Изменения сохранены! Работа менеджера завершена!')
                    break
            else:
                print('Выберите число от 1 до 5, или Q')
            input('*Нажмите Enter для продолжения*')
            print('--------------------------------')


