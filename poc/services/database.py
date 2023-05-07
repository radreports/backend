import requests
import sqlalchemy
import json
from datetime import datetime
from services import studies, models, database

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  services.config import settings
from sqlalchemy.ext.declarative import declarative_base
from services.studies import Base,Studies
# from  config import settings

DATABASE_URI = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def createStudy(study):
    
    db = SessionLocal()
    
    new_study = Studies(**study)
    db.add(new_study)
    db.commit()
    db.refresh(new_study)
    print(new_study)
    return new_study


def getStudies(userID):
    db = SessionLocal()
    print("userID before select::",userID)
    # study = db.query(Studies).all()
    study = db.query(Studies,Studies.user_id == "Demo").all()
    print("Executed query ::",study)
    if study is None:
        raise Exception(status_code=404, detail="Studies not found")
    return study
