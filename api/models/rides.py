from pydantic import BaseModel, Field
from datetime import date
from decimal import Decimal

class Ride(BaseModel):
    id: int
    horse_id: int
    show_id: int
    time: Decimal
    money_earned: Decimal
    ride_date: date
