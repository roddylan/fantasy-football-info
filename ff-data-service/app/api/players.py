# app/api/players.py

from fastapi import APIRouter, Depends
from app.core.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/all')
def get_all_players():
    return {'msg': 'success'}


@router.post('/fill_all')
def fill_players(db: Session = Depends(get_db)):
    pass