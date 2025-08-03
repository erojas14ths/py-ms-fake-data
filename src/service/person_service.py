from src.enums.genre_enum import GenreEnum
from src.repository.person_repository import find_one as find_one_repository, \
    find_all as find_all_repository, \
    find_all_unique as find_all_unique_repository


def find_one(genre: GenreEnum):
    """Find one"""
    return find_one_repository(genre)


def find_all(size: int, unique: bool, genre: GenreEnum):
    """Find all with/without unique data"""
    if unique:
        return find_all_unique_repository(size, genre)
    else:
        return find_all_repository(size, genre)
