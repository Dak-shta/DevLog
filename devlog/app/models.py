from sqlalchemy import Column, Date, Integer, DateTime, Text
from datetime import date, datetime
from .database import Base

class StandUpLog(Base):
    __tablename__="standuplogs"
    id=Column(Integer,primary_key=True,index=True)
    date=Column(Date,default=date.today)
    yesterday=Column(Text)
    today=Column(Text)
    blockers=Column(Text,nullable=True)
    created_at=Column(DateTime,default=datetime.utcnow)