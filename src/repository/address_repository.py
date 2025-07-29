from faker import Faker

from src.model.address import Address


def find_one(fake: Faker, number: str):
    id = fake.unique.uuid4()
    country = fake.country()
    postcode = fake.postcode()
    city = fake.city()
    street_address = fake.street_address()
    return Address(id=id,
                   number=number,
                   country=country,
                   postcode=postcode,
                   city=city,
                   street_address=street_address)
