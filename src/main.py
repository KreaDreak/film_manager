from src import FilmsManager

manager = FilmsManager('src/films_db.json')
# new_film = {'title': 'Uncharted', 'genre': 'action movie', 'year': 2022, 'rating': 6.8}
# manager.add_film('Uncharted', 'action movie', 2022, 6.8)
# print(manager.search_by_rating(8.7))
# print(manager.search_by_genre('Action'))
# manager.del_film("Attack on Titan")
manager.save_db()
# print(manager)
manager.manage()
# print(manager.films)
