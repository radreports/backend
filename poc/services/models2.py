from . database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text,Sequence, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Study(Base):
    __tablename__ = 'studies'
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(String)
    referring_physician_name  = Column(String)
    study_id = Column(String)
    study_instance_uid = Column(String)
    patient_name = Column(String)
    patient_age = Column(String)
    patient_sex = Column(String)
    patient_mrn = Column(String)
    bodypart_examined = Column(String)
    findings = Column(String)
    infer_status = Column(String)
    infer_date = Column(String)
    # def __repr__(self):
    #     return "<Studies(user_id='%s', ReferringPhysicianName='%s', study_id='%s', study_id='%s')>"  
    #     (
    #         self.name,
    #         self.fullname,
    #         self.nickname,
    #     )