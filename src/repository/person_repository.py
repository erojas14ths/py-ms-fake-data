from src.enums.genre_enum import GenreEnum
from src.mapper.person_mapper import map_person_female
from src.mapper.person_mapper import map_person_female_unique
from src.mapper.person_mapper import map_person_male
from src.mapper.person_mapper import map_person_male_unique


def find_one(genre: GenreEnum):
    """Generate data by genre"""
    return map_person_male() if GenreEnum.male == genre else map_person_female()


def find_one_unique(genre: GenreEnum):
    """Generate unique data by genre"""
    return map_person_male_unique() if GenreEnum.male == genre else map_person_female_unique()


def find_all(size: int, genre: GenreEnum):
    """Generate list data by genre"""
    result = []
    for i in range(size):
        item = find_one(genre)
        result.append(item)
    return result


def find_all_unique(size: int, genre: GenreEnum):
    """Generate list unique data by genre"""
    result = []
    try:
        for i in range(size):
            item = find_one_unique(genre)
            result.append(item)
        return result
    except Exception:
        return result
