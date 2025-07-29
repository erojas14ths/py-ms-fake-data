from fastapi import APIRouter

from src.model.address import Address
from src.model.person import Person
from src.service.address_service import find_all as find_all_address
from src.service.person_service import find_all as find_all_persons

router = APIRouter()


@router.get("/persons")
def router_find_all_persons(count: int = 0, unique: bool = False) -> list[Person]:
    return find_all_persons(count, unique)


@router.get("/address")
def router_find_all_address(count: int = 0) -> list[Address]:
    return find_all_address(count)
