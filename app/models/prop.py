from pydantic import BaseModel

class Prop(BaseModel):
    id: str
    name: str
    addr: str
    city: str
    state: str
