# app/schema/players.py

from pydantic import BaseModel
from typing import List

class Player(BaseModel):
    name: str
    pff_id: str
    team: str
    status: str
    