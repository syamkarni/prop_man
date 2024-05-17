from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi import HTTPException
from typing import List
from ..schemas.prop import PropCreate, PropUpdate, PropResp

client = MongoClient("mongodb+srv://ud9211:bEPLXA3jb6tjYw72@cls1.funvk5o.mongodb.net/?retryWrites=true&w=majority&appName=cls1")
db = client.prop_mgmt
prop_col = db.props

def new_prop(prop: PropCreate) -> List[PropResp]:
    prop_dict = prop.dict()
    result = prop_col.insert_one(prop_dict)
    prop_dict["id"] = str(result.inserted_id)
    return list_props()

def get_prop(city: str) -> List[PropResp]:
    props = prop_col.find({"city": city})
    return [PropResp(id=str(p["_id"]), **p) for p in props]

def upd_prop(id: str, prop: PropUpdate) -> List[PropResp]:
    prop_dict = prop.dict()
    result = prop_col.update_one({"_id": ObjectId(id)}, {"$set": prop_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Property not found")
    return list_props()

def get_cities(state: str) -> List[str]:
    props = prop_col.find({"state": state})
    return list(set(p["city"] for p in props))

def get_similar(id: str) -> List[PropResp]:
    prop = prop_col.find_one({"_id": ObjectId(id)})
    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")
    props = prop_col.find({"city": prop["city"]})
    return [PropResp(id=str(p["_id"]), **p) for p in props]

def list_props() -> List[PropResp]:
    props = prop_col.find()
    return [PropResp(id=str(p["_id"]), **p) for p in props]
