# app/services/player_info.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import requests
from typing import Dict, Tuple, List
from bs4 import BeautifulSoup, Tag
from app.models.players import Player
from app.core import enums
from fastapi import status

class PlayerInfoService:
    def __init__(self):
        pass

    def _pfr_web(self, letter: str) -> str:
        assert len(letter) > 0
        return f"https://www.pro-football-reference.com/players/{letter[0].upper()}/"

    def fill_players_table(self, db: Session, year: int = 2024) -> None:
        try:
            for i in range(0, 26):
                letter = chr(ord("a") + i)
                res = requests.get(self._pfr_web(letter.upper()))
                if res.status_code != 200:
                    continue
                html = BeautifulSoup(res.text, 'lxml')
                links: List[Tag] = html.find("div", {"id": "all_players"}).find_all("a")
                # res.close()
                for link in links:
                    player_name = link.text
                    player_id = link.get("href").split("/")[-1].split(".")[0]
                    # active = link.parent.name == "b"
                    pos = res.findall(r"\((.*?)\)", link.next_sibling.strip())[0]

                    try:
                        player = Player(
                            id=player_id,
                            name=player_name,
                            positions=[enums.Position(pos)]
                        )
                        db.add(player)
                        db.commit()
                    except ValueError:
                        # invalid position, non offensive player
                        # skip player
                        continue
                    except IntegrityError:
                        db.rollback()
            return status.HTTP_200_OK
        except Exception:
            return status.HTTP_500_INTERNAL_SERVER_ERROR
        