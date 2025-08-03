from src.repository.person_repository import find_one as find_one_repository, \
    find_all as find_all_repository, \
    find_all_unique as find_all_unique_repository


def find_one():
    """Find one"""
    return find_one_repository()


def find_all(count: int, unique: bool):
    """Find all with/without unique data"""
    if unique:
        return find_all_unique_repository(count)
    else:
        return find_all_repository(count)
