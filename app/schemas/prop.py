from pydantic import BaseModel

class PropCreate(BaseModel):
    name: str
    addr: str
    city: str
    state: str

class PropUpdate(BaseModel):
    name: str
    addr: str
    city: str
    state: str

class PropResp(BaseModel):
    id: str
    name: str
    addr: str
    city: str
    state: str