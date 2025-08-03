from src.mapper.address_mapper import map_address


def find_one():
    """Generate data"""
    return map_address()


def find_all(size: int):
    """Generate list data"""
    result = []
    for i in range(size):
        item = find_one()
        result.append(item)
    return result
