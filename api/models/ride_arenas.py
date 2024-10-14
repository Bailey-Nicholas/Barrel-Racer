from pydantic import BaseModel, Field

class RideArena(BaseModel):
    ride_id: int
    arena_id: int
