from sqlalchemy import Column, Integer, String, TIMESTAMP, func, Date, Decimal
from sqlalchemy.orm import relationship, ForeignKey
from .database import Base


class Ride(Base):
    __tablename__ = "rides"

    id = Column(Integer, primary_key=True, index=True)
    horse_id = Column(Integer, ForeignKey("horses.id", ondelete="CASCADE"), nullable=False)
    show_id = Column(Integer, ForeignKey("shows.id", ondelete="CASCADE"), nullable=False)
    time = Column(Decimal(10, 2))
    money_earned = Column(Decimal(10, 2))
    ride_date = Column(Date, nullable=False)

    horse = relationship("Horse", back_populates="rides")
    show = relationship("Show", back_populates="rides")
