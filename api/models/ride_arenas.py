from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship, ForeignKey
from .database import Base

class RideArena(Base):
    __tablename__ = "ride_arenas"

    ride_id = Column(Integer, ForeignKey("rides.id", ondelete="CASCADE"), primary_key=True)
    arena_id = Column(Integer, ForeignKey("arenas.id", ondelete="CASCADE"), primary_key=True)
