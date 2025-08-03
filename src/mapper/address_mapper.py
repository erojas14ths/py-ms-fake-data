from faker import Faker

from src.model.address import Address

fake = Faker('es_ES')


def map_address():
    """Map address male model"""
    id = fake.uuid4()
    name = fake.address()
    return Address(id=id, name=name)
