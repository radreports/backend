from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from . import models, schemas
from app.core.security import get_password_hash
from  app.core.config import settings

async def delete_study(db,study_id2: str):
    
    print(study_id2)
    # study = db.query(models.Studies,models.Studies.study_id == study_id2).delete()
    # studies = db.query(models.Studies,models.Studies.study_id == study_id2).all()
    studies = db.query(models.Studies).filter(models.Studies.study_id == study_id2).first()
    result = db.delete(studies)
    # result = db.delete(models.Studies,models.Studies.study_instance_uid == study_id)
    db.commit()
    # return {"study_id": result}
    # studies = db.query(models.Studies).all()
    return result

def get_all_studies(db: Session):
    # studies = db.query(models.Studies).all()
    # studies = db.query(models.Studies,models.Studies.user_id == user_id).all()
    studies =  db.query(models.Studies).all()
    print(studies)
    if studies is None:
        raise Exception(status_code=404, detai="Studies not found")
    return studies

def get_studies(db: Session, user_id: str):
    # studies = db.query(models.Studies).all()
    # studies = db.query(models.Studies,models.Studies.user_id == user_id).all()
    studies =  db.query(models.Studies).filter(models.Studies.user_id == user_id).all()
    print(studies)
    if studies is None:
        raise Exception(status_code=404, detai="Studies not found")
    return studies

def update_study_results(db: Session, study: schemas.Study):
    print("updating study results ..",type(study))
    study_id  = study.study_id
    # study['study_id']
    inference_findings = study.inference_findings
    print("Study id::",study_id)
    print("inference_findings::",inference_findings)
    result = db.query(models.Studies).filter(models.Studies.study_id == study_id).update({models.Studies.inference_findings:inference_findings,models.Studies.infer_status:"Complete"}, synchronize_session = False)
    db.commit()

    # session.query(Customers).filter(Customers.id! = 2).
    # update({Customers.name:"Mr."+Customers.name}, synchronize_session = Fals

def create_study(db: Session, study):
    # new_study = models.Studies(**study)
    # new_study = study
    # print("study---",study)
    try:
        new_study = models.Studies(**study)
        db.add(new_study)
        print("study---",study)
        db.commit()
        # db.refresh(**new_study)
    except Exception as e: 
        print("Exception::",str(e))

       

    print("After create study commit--")
    return new_study


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_by_email(db: Session, email: str) -> schemas.UserBase:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.UserOut]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return user


def edit_user(
    db: Session, user_id: int, user: schemas.UserEdit
) -> schemas.User:
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    update_data = user.dict(exclude_unset=True)

    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(user.password)
        del update_data["password"]

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
