from pydantic import BaseModel, Field

class Arena(BaseModel):
    id: int
    name: str
    location:str
