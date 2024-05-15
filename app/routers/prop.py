from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas.prop import PropCreate, PropUpdate, PropResp
from ..srv.prop import (
    new_prop, 
    get_prop, 
    upd_prop, 
    get_cities, 
    get_similar
)

rt = APIRouter()

@rt.post("/props", response_model=List[PropResp])
def add_prop(prop: PropCreate):
    return new_prop(prop)

@rt.get("/props/{city}", response_model=List[PropResp])
def get_props(city: str):
    return get_prop(city)

@rt.put("/props/{id}", response_model=List[PropResp])
def upd_props(id: str, prop: PropUpdate):
    return upd_prop(id, prop)

@rt.get("/cities/{state}", response_model=List[str])
def cities(state: str):
    return get_cities(state)

@rt.get("/props/sim/{id}", response_model=List[PropResp])
def similar_props(id: str):
    return get_similar(id)