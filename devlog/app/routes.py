from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date, timedelta

from .database import SessionLocal
from .models import StandUpLog

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE LOG
@router.post("/logs")
def create_log(
    yesterday: str,
    today: str,
    blockers: str = "",
    db: Session = Depends(get_db)
):
    log = StandUpLog(
        yesterday=yesterday,
        today=today,
        blockers=blockers
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


@router.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    return db.query(StandUpLog).all()


@router.get("/logs/week")
def get_week_logs(db: Session = Depends(get_db)):
    week_ago = date.today() - timedelta(days=7)
    return db.query(StandUpLog).filter(StandUpLog.date >= week_ago).all()