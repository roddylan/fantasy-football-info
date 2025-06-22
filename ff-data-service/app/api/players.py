# app/api/players.py

from fastapi import APIRouter, Depends

router = APIRouter()


@router.get('/all')
def get_all_players():
    return {'msg': 'success'}


@router.post('/fill_all')
def fill_players():
    pass