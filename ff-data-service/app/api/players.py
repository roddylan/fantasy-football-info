# app/api/players.py

from fastapi import APIRouter

router = APIRouter()


@router.get('/all')
def get_all_players():
    pass