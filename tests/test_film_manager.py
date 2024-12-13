import pytest
import json

from src.films_manager import FilmsManager

# Содержимое тестовой базы данных
db_content = [
        {"title": "Chronicles of the Galaxy", "genre": "Adventure", "seasons": 5, "rating": 8.0},
        {"title": "Mystery Island", "genre": "Fantasy", "seasons": 3, "rating": 9.0},
        {"title": "Epic Quest", "genre": "Fantasy", "seasons": 4, "rating": 7.0},
        {"title": "Crime Files", "genre": "Crime Drama", "seasons": 6, "rating": 5.0},
        {"title": "Crime Files 2", "genre": "Crime Drama", "seasons": 6, "rating": 5.0},
        {"title": "Medical Miracles", "genre": "Medical Drama", "seasons": 2, "rating": 8.0},
        {"title": "Time Travelers", "genre": "Adventure", "seasons": 4, "rating": 8.0},
        {"title": "Comedy Central", "genre": "Comedy", "seasons": 7, "rating": 9.0},
        {"title": "Fallout", "genre": "Action", "seasons": 1, "rating": 8.5}
    ]


@pytest.fixture
def temp_db_path(tmp_path):
    # db_file = f'{tmp_path}/tv_shows_db.json'
    db_file = tmp_path / "tv_shows_db.json"
    with open(db_file, 'w', encoding='UTF-8') as f:
        json.dump(db_content, f)
    return str(db_file)


@pytest.fixture
def manager_with_db(temp_db_path):
    manager = FilmsManager(temp_db_path)
    manager.load_db()
    return manager


def test_load_db(manager_with_db: FilmsManager):
    assert len(manager_with_db.films) == len(db_content)
    equal_shows = 0
    for show in db_content:
        if show in manager_with_db.films:
            equal_shows += 1
    assert equal_shows == len(manager_with_db.films)


def test_find_by_genre(manager_with_db: FilmsManager):
    adventure_films = manager_with_db.search_by_genre("Adventure")
    assert len(adventure_films) == 2
    for film in adventure_films:
        assert film['genre'] == 'Adventure'


def test_find_by_rating(manager_with_db: FilmsManager):
    rating_films = manager_with_db.search_by_rating(7.1)
    assert len(rating_films) == 6
    for film in rating_films:
        assert film['rating'] >= 7.1


def test_add_film(manager_with_db: FilmsManager):
    film = {"title": "da", "genre": "net", "year": 2005, "rating": 8.1}
    init_len = len(manager_with_db.films)
    manager_with_db.add_film(**film)
    assert init_len + 1 == len(manager_with_db.films)
    assert film in manager_with_db.films


def test_del_film(manager_with_db: FilmsManager):
    film_title = 'Crime Files'
    init_len = len(manager_with_db.films)
    assert manager_with_db.del_film(film_title)
    assert init_len - 1 == len(manager_with_db.films)
    for film in manager_with_db.films:
        assert film_title != film['title']


def test_save_db(manager_with_db: FilmsManager):
    film = {"title": "da", "genre": "net", "year": 2005, "rating": 8.1}
    init_len = len(manager_with_db.films)
    manager_with_db.add_film(**film)
    manager_with_db.save_db()
    manager_with_db.load_db()
    after_len = len(manager_with_db.films)
    assert after_len == init_len + 1
    assert film in manager_with_db.films


