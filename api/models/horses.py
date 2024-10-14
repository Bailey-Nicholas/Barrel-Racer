from pydantic import BaseModel, Field
from typing import Optional

class Horse(BaseModel):
    id: int
    name: str
    breed: Optional[str]
    age: Optional[int]
    owner_id: Optional[int]
