from pydantic import BaseModel
import typing as t
from datetime import datetime, date

class UserBase(BaseModel):
    email: str
    is_active: bool = True
    is_superuser: bool = False
    first_name: str = None
    last_name: str = None


class UserOut(UserBase):
    pass


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserEdit(UserBase):
    password: t.Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
    permissions: str = "user"



class StudyCreate(BaseModel):
    user_id: str
    referring_physician_name: str
    study_id: str
    study_instance_uid: str
    patient_name: str
    patient_age: str
    patient_sex: str
    patient_mrn:str
    bodypart_examined: str
    inference_findings: str
    infer_status: str
    infer_date: str
    reviewer_id:str
    reviewer_name: str
    review_date: datetime
    review_status: bool
    review_report:str
    AccessionNumber:str

class StudyUpdate(BaseModel):
    user_id: str
    referring_physician_name: str
    study_id: str
    study_instance_uid: str
    patient_name: str
    patient_age: str
    patient_sex: str
    patient_mrn:str
    bodypart_examined: str
    inference_findings: str
    infer_status: str
    infer_date: str
    reviewer_id:str
    reviewer_name: str
    review_date: datetime
    review_status: bool
    review_report:str

class Study(BaseModel):
    study_id: str
    inference_findings: str
   