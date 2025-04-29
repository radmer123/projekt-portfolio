"""Funkcje pomocnicze SQLAlchemy do obsługi testowania"""
import pytest
from datetime import date

import crud
from database import SessionLocal

# Aby przetestować min_last_changed_date, użyj daty testowej 1/4/2024.
test_date = date(2024,4,1)

@pytest.fixture(scope="function")
def db_session():
    """Ustanawia połączenie bazy danych i zamyka je po zakończeniu korzystania"""
    session = SessionLocal()
    yield session
    session.close()

def test_get_player(db_session):
    """Sprawdza, czy można pobrać pierwszego gracza"""
    player = crud.get_player(db_session, player_id = 1001)
    assert player.player_id == 1001

def test_get_players(db_session):
    """Sprawdza, czy liczba graczy w bazie danych jest zgodna z oczekiwaniami."""
    players = crud.get_players(db_session, skip=0, limit=10000,
                                min_last_changed_date=test_date)
    assert len(players) == 1018

def test_get_players_by_name(db_session):
    """Sprawdza, czy liczba graczy w bazie danych jest zgodna z oczekiwaniami."""
    players = crud.get_players(db_session, first_name="Bryce", last_name="Young")
    assert len(players) == 1
    assert players[0].player_id == 2009


def test_get_all_performances(db_session):
    """Sprawdza, czy liczba występów w bazie danych jest zgodna z oczekiwaniami — tzn. czy uwzględnia wszystkie występy"""
    performances = crud.get_performances(db_session, skip=0, limit=18000)
    assert len(performances) == 17306

def test_get_new_performances(db_session):
    """Sprawdza, czy liczba występów w bazie danych jest zgodna z oczekiwaniami."""
    performances = crud.get_performances(db_session, skip=0, limit=10000, 
                                         min_last_changed_date=test_date)
    assert len(performances) == 2711

#testowanie funkcji zliczania
def test_get_player_count(db_session):
    player_count = crud.get_player_count(db_session)
    assert player_count == 1018
