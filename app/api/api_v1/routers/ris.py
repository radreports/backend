from fastapi import APIRouter,Header,BackgroundTasks, Request, Depends, Response, encoders, File, UploadFile,BackgroundTasks, WebSocket
import typing as t
from typing import List, Optional,Union
import requests,json
# from . import ServiceRequest 
from app.core import config

import fhirclient.models.patient as p
import fhirclient.models.diagnosticreport as d_report
import fhirclient.models.servicerequest as sr
from fhirclient import client

import fhirclient.models.humanname as hn
import fhirclient.models.coding as coding

from . import api_helper as helper
ris_router = r = APIRouter()
OrthancURL = config.Settings.ORTHANC_URL
fhirURL = config.Settings.FHIR_URL

settings = {
    'app_id': 'my_web_app',
    'api_base': fhirURL
}
smart = client.FHIRClient(settings=settings)


@r.get("/Patient")
async def get_Patients():
    return helper.get_Patients()

@r.get("/Patient/{patient_id}")
async def get_patient_id(patient_id: str):
    return helper.get_patient_id(patient_id)


@r.post("/Patient")
async def set_Patient(request: Request):
    
    return  helper.set_Patient(Request)

@r.delete("/Patient/{patient_id}")
async def del_patient_id(patient_id: str):
    return helper.del_patient_id(patient_id)

@r.put("/Patient/{patient_id}")
async def put_patient_id(patient_id: str):
    return helper.put_patient_id(patient_id)

@r.get("/Practitioner")
async def get_Practitionar():
    return helper.get_Practitionars()

@r.get("/Practitioner/{Practitionar_id}")
async def get_Practitionar_id(Practitionar_id: str):
    return helper.get_practitionar_id(Practitionar_id)


@r.post("/Practitioner")
async def set_Practitionar(request: Request):
    sr = await request.json()
    return  helper.set_Practitionar(sr)

@r.delete("/Practitioner/{practitionar_id}")
async def del_practitionar_id(practitionar_id: str):
    return helper.del_practitionar_id(practitionar_id)

@r.put("/Practitioner/{practitionar_id}")
async def put_practitionar_id(practitionar_id: str):
    return helper.put_practitionar_id(practitionar_id)


@r.get("/ServiceRequest")
async def get_ServiceRequest():
    
    return helper.get_ServiceRequest()

@r.get("/ServiceRequest/{service_request_id}")
async def get_service_request_id(service_request_id: str):
   return helper.get_service_request_id(service_request_id)

@r.post("/ServiceRequest")
async def set_ServiceRequest(request: Request):
    # print(await request.json())
    sr = await request.json()
    # return request
    return   helper.set_ServiceRequest(sr)

@r.put("/ServiceRequest/{service_request_id}")
async def put_service_request_id(service_request_id: str):
    return helper.put_service_request_id(service_request_id)

@r.get("/DiagnosticReport/")
async def getDiagnosticReports(response: Response):
    return helper.getDiagnosticReports(response)
    
@r.get("/DiagnosticReport/{diagnostic_report_id}")
async def get_diagnostic_report_request_id(diagnostic_report_id: str):
    return helper.get_diagnostic_report_request_id(diagnostic_report_id)

@r.post("/DiagnosticReport")
async def set_DiagnosticReport(request: Request):
    sr = await request.json()
    return  helper.set_DiagnosticReport(sr)

@r.put("/DiagnosticReport/{diagnostic_report_id}")
async def put_diagnostic_report_request_id(diagnostic_report_id: str):
    return helper.put_diagnostic_report_request_id(diagnostic_report_id)


@r.get("/ImagingStudy")
async def getImagingStudy():
    return helper.get_ImagingStudy()

@r.get("/ImagingStudy/{id}")
async def get_imaginstudy_id(id: str):
    return helper.get_imaginstudy_id(id)

@r.post("/ImagingStudy/upload")
async def upload_files(files: List[UploadFile],response: Response,ServiceRequest_id:Union[str, None] = Header(default=None, convert_underscores=False)):
    print("Starting backgoung task ...",ServiceRequest_id)
    # userID = "test"
    # background_tasks.add_task(doWorkFlow,files,ServiceRequest_id)
    return await helper.uploadFiles(files,ServiceRequest_id)
