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


class Team(Enum):
    ARI = "ARI"
    ATL = "ATL"
    BAL = "BAL"
    BUF = "BUF"
    CAR = "CAR"
    CHI = "CHI"
    CIN = "CIN"
    CLE = "CLE"
    DAL = "DAL"
    DEN = "DEN"
    DET = "DET"
    GB = "GB"
    HOU = "HOU"
    IND = "IND"
    JAX = "JAX"
    KC = "KC"
    LV = "LV"
    LAC = "LAC"
    LAR = "LAR"
    MIA = "MIA"
    MIN = "MIN"
    NE = "NE"
    NO = "NO"
    NYG = "NYG"
    NYJ = "NYJ"
    PHI = "PHI"
    PIT = "PIT"
    SF = "SF"
    SEA = "SEA"
    TB = "TB"
    TEN = "TEN"
    WAS = "WAS"
