import requests
from services import  database
import json

async def uploadFiles(files,userID,orthanc,OrthancURL):
    print("uploading files .....")
    url = OrthancURL + "/instances"
    
    response  = ""
    for file in files:
        print("file name::",file.filename)
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

    # StudyDate , StudyTime ,LastUpdate ,ReferringPhysicianName
    MainDicomTags = patient['MainDicomTags']
    AccessionNumber = MainDicomTags["AccessionNumber"]
    
    ReferringPhysicianName = MainDicomTags["ReferringPhysicianName"]
    
    StudyDate = MainDicomTags["StudyDate"]
    
    StudyInstanceUID = MainDicomTags["StudyInstanceUID"]

    StudyTime = MainDicomTags["StudyTime"]

    # StudyInstanceUID = patient["StudyInstanceUID"]
    # print("StudyInstanceUID :: ",StudyInstanceUID)
    # Series = patient["Series"]
    # print("Series :: ",Series)
    PatientMainDicomTags = patient['PatientMainDicomTags']
    PatientName = PatientMainDicomTags["PatientName"]
    
    PatientBirthDate = PatientMainDicomTags["PatientBirthDate"]
    
    PatientID = PatientMainDicomTags["PatientID"]
    
    PatientSex = PatientMainDicomTags["PatientSex"]
    # schemas1 = schemas.CreateStudySchema()
    study = {
        "bodypart_examined" : "",
        "patient_sex" : "",
        "infer_date" : "",
        "patient_name" : PatientName,
        "patient_mrn" : PatientID,
        "findings" : "",
        "infer_status" : "",
        "patient_age" : PatientBirthDate,
        "referring_physician_name" : ReferringPhysicianName,
        "study_id" : ParentStudy,
        "study_instance_uid" : StudyInstanceUID,
        "user_id" : userID
    
    }
    val = database.createStudy(study)
   
    return val
