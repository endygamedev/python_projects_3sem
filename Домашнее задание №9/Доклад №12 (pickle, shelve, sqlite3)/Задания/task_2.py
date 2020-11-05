"""
    С помощью shelve создайте файл "MyFavoriteMovies", и запишите в него названия своих любимых фильмов.
    В качестве ключей используйте имена режисеров
"""

import shelve


with shelve.open('MyFavoriteMovies') as films:
    films['Robert Zemeckis'] = 'Back to the Future Part II'
    films['George Lucas'] = 'Star Wars: Episode III - Revenge of the Sith'
    films['Guy Ritchie'] = 'The Gentlemen'