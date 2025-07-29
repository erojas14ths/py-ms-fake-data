from pydantic import BaseModel


class Address(BaseModel):
    id: str
    number: str
    country: str
    postcode: str
    city: str
    street_address: str
