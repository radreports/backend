from fastapi import APIRouter,Header,BackgroundTasks, Request, Depends, Response, encoders, File, UploadFile,BackgroundTasks, WebSocket
import typing as t
from typing import List, Optional,Union
from app.db.session import get_db
from fhirclient import client
import requests
from app.db.crud import (
    get_studies,
    get_all_studies,
   create_study,
   delete_study,
   update_study_results
    
)
from app.db.schemas import StudyCreate
# , StudyUpdate
# from app.core.auth import get_current_active_user, get_current_active_superuser
from app.util import dicom_uploader
from beren import Orthanc
from app.core import config
from pydantic import BaseModel
from app.db.schemas import Study
import fhirclient.models.patient as p
import fhirclient.models.diagnosticreport as d_report
# import fhirclient.models.
import json
studies_router = r = APIRouter()
OrthancURL = config.Settings.ORTHANC_URL
fhirURL = config.Settings.FHIR_URL
orthanc = Orthanc(OrthancURL)
settings = {
    'app_id': 'my_web_app',
    'api_base': fhirURL
}
smart = client.FHIRClient(settings=settings)


# @r.get("/Patient")
# async def get_Patient():
#     response2 =  requests.get(fhirURL+"/fhir/ServiceRequest?_pretty=true")
#     patient = p.Patient.read('bundle', smart.server)
#     # p.Patient.bundle(smart.server)
#     res = json.loads(response2.text)
    
#     # print(res)
#     return res
# @r.post("/Patient")
# async def set_Patient(request: Request):
#     return await request.json()


# @r.get("/ServiceRequest")
# async def get_ServiceRequest():
#     response2 =  requests.get(fhirURL+"/fhir/ServiceRequest?_pretty=true")
#     res = json.loads(response2.text)

#     # print(res)
#     return res
# @r.post("/ServiceRequest")
# async def set_ServiceRequest(request: Request):
#     return await request.json()



# @r.get("/DiagnosticReport/")
# async def getDiagnosticReports(response: Response):
#     print("")
#     #  http://localhost:8080/hapi-fhir-jpaserver/fhir/DiagnosticReport?_pretty=true
#     response2 =  requests.get(fhirURL+"/fhir/DiagnosticReport?_pretty=true")
#     res = json.loads(response2.text)
#     print(res)
#     return res
    


@r.get("/studies/all")
async def getAllStudies(response: Response,userID: Union[str, None] = Header(default=None, convert_underscores=False), Authorization: Union[str, None] = Header(default=None, convert_underscores=False),db=Depends(get_db)):
    # db= get_db()
    studies = get_all_studies(db)
    print(studies)
    return studies


@r.get("/studies")
async def getStudies(response: Response,userID: Union[str, None] = Header(default=None, convert_underscores=False), Authorization: Union[str, None] = Header(default=None, convert_underscores=False),db=Depends(get_db)):
    # db= get_db()
    studies = get_studies(db,userID)
    print(studies)
    return studies

async def doWorkFlow(files,Task):
    print("starting file upload ..")
   
    await dicom_uploader.uploadFiles(files,Task,orthanc,OrthancURL)
# 

# @r.post("/ImagingStudy")
# async def upload_files(files: List[UploadFile], background_tasks: BackgroundTasks,response: Response,Task:Union[str, None] = Header(default=None, convert_underscores=False),userID: Union[str, None] = Header(default=None, convert_underscores=False), Authorization: Union[str, None] = Header(default=None, convert_underscores=False)):
#     print("Starting backgoung task ...")
#     # userID = "test"
#     background_tasks.add_task(doWorkFlow,files,Task)

@r.delete("/studies/{study_id}")
async def deletestudy(study_id: str,db=Depends(get_db)):
    print("Delete::",study_id)
    orthanc.delete_study(study_id)
    response = await delete_study(db,study_id)

    return response

@r.put("/studies")
async def updateStudies(study: Study,db=Depends(get_db)):
    # print("study id ::",study_id)
    print("Study::",study)
    update_study_results(db, study)
    return study