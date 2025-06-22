# app/models/players.py

from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum, Integer, ForeignKey
from typing import List
from app.core.enums import Position, PlayerStatus

class Player(Base):
    __tablename__ = "player"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    positions: Mapped[List[Position]] = mapped_column(List[Enum(Position)])
    

class PlayerStatusModel(Base):
    __tablename__ = 'player_status'
    player_id: Mapped[str] = mapped_column(ForeignKey("player.id"), primary_key=True)
    year: Mapped[int] = mapped_column(primary_key=True)
    week: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[PlayerStatus] = mapped_column(Enum(PlayerStatus))
    
    
    player_id = relationship("Player", primary_key=True)
    