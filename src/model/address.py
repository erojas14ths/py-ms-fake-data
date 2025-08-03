from pydantic import BaseModel


class Address(BaseModel):
    id: str
    name: str
