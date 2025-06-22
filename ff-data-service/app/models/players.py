# app/models/players.py

from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum, Integer, ForeignKey
from typing import List
from app.core import enums

class Player(Base):
    __tablename__ = "player"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    positions: Mapped[List[enums.Position]] = mapped_column(List[Enum(enums.Position)])
    

class PlayerStatus(Base):
    __tablename__ = 'player_status'
    player_id: Mapped[str] = mapped_column(ForeignKey("player.id"), primary_key=True)
    year: Mapped[int] = mapped_column(primary_key=True)
    week: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[enums.PlayerStatus] = mapped_column(Enum(enums.PlayerStatus))
    
    
    player_id = relationship("Player", primary_key=True)
    
    
class PlayerTeam(Base):
    __tablename__ = 'player_team'
    player_id: Mapped[str] = mapped_column(ForeignKey("player.id"), primary_key=True)
    year: Mapped[int] = mapped_column(primary_key=True)
    week: Mapped[int] = mapped_column(primary_key=True)
    team: Mapped[enums.Team] = mapped_column(Enum(enums.Team))
    