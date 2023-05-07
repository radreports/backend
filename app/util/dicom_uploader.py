import requests
import json
from app.db.session import get_db
from app.db.crud import (
    get_studies,
   create_study,
    
)
from  app.core.config import settings
import redis
import json
from app.db.schemas import StudyCreate
# , StudyUpdate

async def uploadFiles(files,db,userID,Task,orthanc,OrthancURL):
    print("uploading files for task  .....",Task)
    url = OrthancURL + "/instances"
    
    response  = ""
    for file in files:
        # print("file name::",file.filename)
        # filename = secure_filename(file.filename)
        data = await file.read()
        response2 =  requests.post(url,data=data, headers={'Content-Type': 'application/octet-stream'},verify=False)
        # print(response2.text)
        response  = response2.text
        # print(response)

    print(response)
    study = json.loads(response)
    # Series = study["Series"]
    ParentPatient = study["ParentPatient"]
    
    ParentStudy = study["ParentStudy"]
    
    studies = orthanc.get_study(ParentStudy)
    # patient = json.loads(studies)
    patient = studies
    print("studies ...",studies)
    Series = patient['Series']

    # StudyDate , StudyTime ,LastUpdate ,ReferringPhysicianName
    MainDicomTags = patient['MainDicomTags']
    print("before .....")
    try:
        AccessionNumber = MainDicomTags["AccessionNumber"]
    except Exception as e: 
        print("Exception::",str(e))
        AccessionNumber = ""

    # AccessionNumber = MainDicomTags["AccessionNumber"]
    print("After .....")
    try:
     ReferringPhysicianName = MainDicomTags["ReferringPhysicianName"]
    except Exception as e: 
         print("Exception::",str(e))
         ReferringPhysicianName = ""
    
    try:
        StudyDate = MainDicomTags["StudyDate"]
    except Exception as e: 
        
        print("Exception::",str(e))
    try:
        StudyInstanceUID = MainDicomTags["StudyInstanceUID"]
    except Exception as e: 
        StudyInstanceUID = ""
        print("Exception::",str(e))
    try:
     StudyTime = MainDicomTags["StudyTime"]
    except Exception as e: 
        StudyTime = ""
        print("Exception::",str(e))
    # StudyInstanceUID = patient["StudyInstanceUID"]
    # print("StudyInstanceUID :: ",StudyInstanceUID)
    # Series = patient["Series"]
    # print("Series :: ",Series)

    try:
        PatientMainDicomTags = patient['PatientMainDicomTags']
    except Exception as e: 
        print("Exception::",str(e))
    
    try:
        PatientName = PatientMainDicomTags["PatientName"]
    except Exception as e: 
        print("Exception::",str(e))
    try:
        PatientSex =  PatientMainDicomTags["PatientName"]
    except Exception as e: 
        print("Exception::",str(e))

    try:
        PatientBirthDate = PatientMainDicomTags["PatientBirthDate"]
    except Exception as e: 
        print("Exception::",str(e))
    
    try:
        PatientID = PatientMainDicomTags["PatientID"]
    except Exception as e: 
        print("Exception::",str(e))

    try:
        PatientSex = PatientMainDicomTags["PatientSex"]
    except Exception as e: 
        print("Exception::",str(e))
    # schemas1 = schemas.CreateStudySchema()
    # study = {
    #     "bodypart_examined" : "",
    #     "patient_sex" : "",
    #     "infer_date" : "",
    #     "patient_name" : PatientName,
    #     "patient_mrn" : PatientID,
    #     "findings" : "N/A",
    #     "infer_status" : "In Progress",
    #     "patient_age" : PatientBirthDate,
    #     "referring_physician_name" : ReferringPhysicianName,
    #     "study_id" : ParentStudy,
    #     "study_instance_uid" : StudyInstanceUID,
    #     "user_id" : userID
    
    # }
    try:
        study = {
            "user_id": userID,
            "referring_physician_name": ReferringPhysicianName,
            "study_id": ParentStudy,
            "study_instance_uid": StudyInstanceUID,
            "patient_name": PatientName,
            "patient_age": PatientBirthDate,
            "patient_sex": PatientSex,
            "patient_mrn":PatientID,
            "bodypart_examined": Task,
            "inference_findings": "N/A",
            "infer_status": "In Progress",
            "infer_date": None,
            "reviewer_id":"None",
            "reviewer_name": "None",
            "review_date": None,
            "review_status": False,
            "review_report":"None",
            "AccessionNumber":AccessionNumber,


        }

    except Exception as e: 
        print("Exception::",str(e))
        study = {}
    print("Update db",study)
    val = create_study(db,study)
    print("before publish ....")
#    OrthancURL

    # red = redis.StrictRedis(settings.REDIS_HOST,settings.REDIS_PORT,password=settings.REDIS_PASSWORD,charset="utf-8",decode_responses=True)
    red = redis.StrictRedis('35.202.115.123',6379,password="m0bdat",charset="utf-8",decode_responses=True)
    res = {
        "Task": Task,
        "pacs_url": OrthancURL,
        "study_id": ParentStudy,
        "Series": Series
    }
    red.publish("test",json.dumps(res))
    print("after publish ....")
    return val
