from src.repository.address_repository import find_one as find_one_repository, \
    find_all as find_all_repository


def find_one():
    """Find one"""
    return find_one_repository()


def find_all(size: int):
    """Find all data"""
    return find_all_repository(size)
