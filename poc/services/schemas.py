from datetime import datetime
from typing import List

from pydantic import BaseModel


class StudiesBaseSchema(BaseModel):
    user_id : str
    study_id : str
    study_instance_uid : str
    patient_name : str
    patient_age : str
    patient_sex  : str
    patient_mrn : str
    bodypart_examined : str
    findings : str
    infer_status : str 
    infer_date : str
    referring_physician_name : str

    class Config:
        orm_mode = True
    

class CreateStudySchema(StudiesBaseSchema):
    pass