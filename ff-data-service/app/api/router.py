# app/api/router.py

from fastapi import APIRouter
from app.api import players

router = APIRouter()


router.include_router(players.router, prefix='/players', tags=['player'])