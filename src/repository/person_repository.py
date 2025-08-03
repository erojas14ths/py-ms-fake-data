from src.mapper.person_mapper import map_person
from src.mapper.person_mapper import map_person_unique


def find_one():
    """Find one without unique data"""
    return map_person()


def find_one_unique():
    """Find one with unique data"""
    return map_person_unique()


def find_all(count: int):
    """Find all without unique data"""
    result = []
    for i in range(count):
        item = find_one()
        result.append(item)
    return result


def find_all_unique(count: int):
    """Find all with unique data"""
    result = []
    try:
        for i in range(count):
            item = find_one_unique()
            result.append(item)
    except Exception as ex:
        return result
