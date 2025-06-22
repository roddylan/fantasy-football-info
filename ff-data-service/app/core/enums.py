# app/core/enums.py

from enum import Enum

class PlayerStatus(Enum):
    H = "H"
    O = "O"
    IR = "IR"
    NA = "NA"
    
    
class Position(Enum):
    QB = "QB"
    WR = "WR"
    RB = "RB"
    TE = "TE"
    K = "K"
    DST = "D/ST"