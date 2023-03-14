from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        interesting_movies = filter(
            lambda movie: movie["rating_kinopoisk"]
            and float(movie["rating_kinopoisk"]) > 0
            and movie["country"].count(",") > 0,
            list_of_movies,
        )
        scores = map(lambda movie: float(movie["rating_kinopoisk"]), interesting_movies)

        total_score: float = 0
        count: int = 0
        for score in scores:
            count += 1
            total_score += score
        return total_score / count

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        interesting_movies = filter(
            lambda movie: movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) >= rating,
            list_of_movies,
        )
        count_of_i = map(lambda movie: movie["name"].count("и"), interesting_movies)
        return sum(count_of_i)
