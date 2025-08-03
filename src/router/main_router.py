from fastapi import APIRouter

from src.model.person import Person
from src.service.person_service import find_one as find_one_service, find_all as find_all_service

router = APIRouter()


@router.get("/person")
def router_find_all_persons() -> Person:
    return find_one_service()


@router.get("/persons")
def router_find_all_persons(count: int = 0, unique: bool = False) -> list[Person]:
    return find_all_service(count, unique)
