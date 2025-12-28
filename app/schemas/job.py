from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    name: str
    owner_id: int

class JobRead(BaseModel):
    id: int
    name: str
    status: str
    owner_id: int

    class Config:
        orm_mode = True