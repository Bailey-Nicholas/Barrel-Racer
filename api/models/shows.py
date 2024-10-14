from pydantic import BaseModel, conint, constr, Field
from datetime import date

class Show(BaseModel):
    id: int
    name: str
    location: str
    show_date: date
