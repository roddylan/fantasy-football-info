# app/schema/players.py

from pydantic import BaseModel
from typing import List
from app.core.enums import PlayerStatus

class Player(BaseModel):
    name: str
    pff_id: str
    team: str
    status: PlayerStatus
    