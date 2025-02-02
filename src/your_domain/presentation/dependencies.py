from fastapi import Depends
from sqlalchemy.orm import Session

from src.your_domain.infrastructure.database import get_db_session
from src.your_domain.infrastructure.event_bus import EventBus

def get_db(session: Session = Depends(get_db_session)):
    try:
        yield session
    finally:
        session.close()

def get_event_bus(event_bus: EventBus = Depends(EventBus)):
    return event_bus
