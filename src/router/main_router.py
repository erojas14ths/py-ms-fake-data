from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from src.enums.genre_enum import GenreEnum
from src.model.address import Address
from src.model.person import Person
from src.service.address_service import find_one as find_one_address_service, find_all as find_all_address_service
from src.service.person_service import find_one as find_one_person_service, find_all as find_all_person_service

router = APIRouter()


@router.get("/person")
def router_find_one_person(genre: GenreEnum = Query(default=GenreEnum.male)) -> Person:
    return find_one_person_service(genre)


@router.get("/persons")
def router_find_all_person(size: int = 0, unique: bool = False, genre: GenreEnum = Query(default=GenreEnum.male)) -> list[
    Person]:
    return find_all_person_service(size, unique, genre)


@router.get("/address")
def router_find_one_address() -> Address:
    return find_one_address_service()


@router.get("/addresses")
def router_find_all_address(size: int = 0) -> list[Address]:
    return find_all_address_service(size)


@router.get("/health")
def health():
    return JSONResponse(content={"status": "ok"})