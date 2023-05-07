from sqlalchemy import Boolean, Column, Integer, String, DateTime, Sequence

from .session import Base
from sqlalchemy.ext.declarative import declarative_base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

# Base = declarative_base()

# Define request and response models for API
# class Studies(Base):
#     __tablename__ = 'studies'
#     id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
#     user_id = Column(String)
#     referring_physician_name = Column(String)
#     study_id = Column(String)
#     study_instance_uid = Column(String)
#     patient_name = Column(String)
#     patient_age = Column(String)
#     patient_sex = Column(String)
#     patient_mrn = Column(String)
#     bodypart_examined = Column(String)
#     findings = Column(String)
#     infer_status = Column(String)
#     infer_date = Column(String)
#     reviewer_id:Column(String)
#     reviewer_name: Column(String, nullable=True)
#     review_date: Column(DateTime, nullable=True)
#     review_status: Column(Boolean, nullable=True)
#     review_report:Column(String, nullable=True)


class Studies(Base):
    __tablename__ = "studies"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id =  Column(String)
    referring_physician_name= Column(String)
    study_id= Column(String)
    study_instance_uid= Column(String)
    patient_name= Column(String)
    patient_age= Column(String)
    patient_sex= Column(String)
    patient_mrn= Column(String)
    bodypart_examined= Column(String, nullable=True)
    inference_findings= Column(String, nullable=True)
    infer_status= Column(String, nullable=True)
    infer_date= Column(String, nullable=True)
    reviewer_id=Column(String, nullable=True)
    reviewer_name= Column(String, nullable=True)
    review_date= Column(DateTime, nullable=True)
    review_status= Column(Boolean, nullable=True)
    review_report=Column(String, nullable=True)
    AccessionNumber=Column(String, nullable=True)
