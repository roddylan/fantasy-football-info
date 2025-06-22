# app/models/players.py

from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from typing import List
from app.core import enums

class Player(Base):
    __tablename__ = "player"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    positions: Mapped[List[enums.Position]] = mapped_column(ARRAY(Enum(enums.Position, name="position_enum", create_type=True)))
    

class PlayerStatus(Base):
    __tablename__ = 'player_status'
    player_id: Mapped[str] = mapped_column(ForeignKey("player.id"), primary_key=True)
    year: Mapped[int] = mapped_column(primary_key=True)
    week: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[enums.PlayerStatus] = mapped_column(Enum(enums.PlayerStatus))
    
    
    player_id = relationship("Player")
    
    
class PlayerTeam(Base):
    __tablename__ = 'player_team'
    player_id: Mapped[str] = mapped_column(ForeignKey("player.id"), primary_key=True)
    year: Mapped[int] = mapped_column(primary_key=True)
    week: Mapped[int] = mapped_column(primary_key=True)
    team: Mapped[enums.Team] = mapped_column(Enum(enums.Team))
    