# app/api/players.py

from fastapi import APIRouter, Depends
from app.core.dependencies import get_db
from sqlalchemy.orm import Session
from app.services.player_info import PlayerInfoService
from typing import Optional
from fastapi import Response

router = APIRouter()


@router.get('/all')
def get_all_players():
    return {'msg': 'success'}


@router.post('/fill_players')
def fill_players(db: Session = Depends(get_db)):
    service = PlayerInfoService()
    result = service.fill_players_table(db=db)
    return Response(status_code=result)
        

@router.post('/fill_player')
def fill_players(player_name: str, db: Session = Depends(get_db)):
    pass