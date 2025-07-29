from src.repository.person_repository import find_one
from faker.exceptions import UniquenessException
from faker import Faker

fake = Faker('es_ES')

def find_all(count: int, unique: bool):
    result = []
    try:
        for i in range(count):
            number = i +1
            item = find_one(fake, str(number), unique)
            result.append(item)
    except UniquenessException:
        print("Error al obtener valores unicos, resetenado los valores únicos.")
        fake.unique.clear()
    return result

