from app.core import config
import typing as t
from typing import List, Optional,Union
import requests,json
from fastapi import APIRouter,Header,BackgroundTasks, Request, Depends, Response, encoders, File, UploadFile,BackgroundTasks, WebSocket
import fhirclient.models.patient as p
import fhirclient.models.diagnosticreport as d_report
import fhirclient.models.servicerequest as sr
import fhirclient.models.imagingstudy as imaging_s
from  fhirclient.models.imagingstudy import ImagingStudySeries as StudySeries
# import fhirclient.models.reference as ref
import fhirclient.models.fhirreference as ref
import fhirclient.models.fhirdate as fhir_date
import fhirclient.models.annotation as fhir_annotation
import fhirclient.models.coding as coding
from datetime import datetime
from fhirclient import client

import fhirclient.models.humanname as hn
import fhirclient.models.coding as coding
# from . import ServiceRequest
import redis
from beren import Orthanc
fhirURL = config.Settings.FHIR_URL

OrthancURL = config.Settings.ORTHANC_URL
apiURL = config.Settings.API_URL
fhir_url = config.Settings.FHIR_URL
redis_url = config.Settings.REDIS_HOST
orthanc = Orthanc(OrthancURL)
settings = {
    'app_id': None,
    'api_base': fhirURL
}
smart = client.FHIRClient(settings=settings)

def get_Patients():
    print("patient called",fhirURL)
    response2 =  requests.get(fhirURL+"/Patient")
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res

def get_patient_id(patient_id: str):
    response2 =  requests.get(fhirURL+"/Patient/"+patient_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res

def get_patient_name(patient_id: str):
    response2 =  requests.get(fhirURL+"/Patient/"+patient_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res

def set_Patient(request: Request):
    
    # patient = p.Patient()
    patient = p.Patient({'id': 'patient-1'})
    name = hn.HumanName()
    name.given = ['Peter']
    name.family = 'Parker'
    patient.name = [name]
    patient.as_json()
    # prints patient's JSON representation, now with id and name

    name.given = ['Peter']
    print(patient.as_json())
    response2 =  requests.post(fhirURL+"/Patient", json=patient.as_json())
    res = json.loads(response2.text)
    return  res

    # return  request.json()

def del_patient_id(patient_id: str):
    response2 =  requests.delete(fhirURL+"/Patient/"+patient_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res


def put_patient_id(patient_id: str):
    response2 =  requests.put(fhirURL+"/Patient/"+patient_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res


def get_Practitionars():
    print("patient called",fhirURL)
    response2 =  requests.get(fhirURL+"/Practitioner")
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res

def get_practitionar_id(practitionar_id: str):
    response2 =  requests.get(fhirURL+"/Practitioner/"+practitionar_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res


def set_Practitionar(request: Request):
    print(fhirURL+"/Practitioner")
    response2 =  requests.post(fhirURL+"/Practitioner", json=request)
    res = json.loads(response2.text)
    return  res


def del_practitionar_id(practitionar_id: str):
    response2 =  requests.delete(fhirURL+"/Practitioner/"+practitionar_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res


def put_practitionar_id(practitionar_id: str):
    response2 =  requests.put(fhirURL+"/Practitioner/"+practitionar_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res


def get_ServiceRequest():
    response2 =  requests.get(fhirURL+"/ServiceRequest")
    res = json.loads(response2.text)

    # print(res)
    return res


def get_service_request_id(service_request_id: str):
    print("service_request_id::",service_request_id)
    response2 =  requests.get(fhirURL+"/ServiceRequest/"+service_request_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res

def set_ServiceRequest(sr):

    response2 =  requests.post(fhirURL+"/ServiceRequest", json=sr)
    res = json.loads(response2.text)
    return  res


def put_service_request_id(service_request_id: str):
    response2 =  requests.put(fhirURL+"/ServiceRequest/"+service_request_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res


def getDiagnosticReports(response: Response):
    print("")
    # fhirclient.
    d_report.DiagnosticReport.read_from( smart.server)
    # report = d_report.DiagnosticReport.read(None, smart.server)
    # smart.request("/DiagnosticReport")
    # search = search.include('subject')
    #  http://localhost:8080/hapi-fhir-jpaserver/fhir/DiagnosticReport?_pretty=true
    response2 =  requests.get(fhirURL+"/DiagnosticReport?_pretty=true")
    res = json.loads(response2.text)
    print(res)
    return res
    

def get_diagnostic_report_request_id(diagnostic_report_id: str):
    response2 =  requests.get(fhirURL+"/DiagnosticReport/"+diagnostic_report_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res

def set_DiagnosticReport(sr):
    print("Post DiagnosticReport::",sr)
    response2 =  requests.post(fhirURL+"/DiagnosticReport", json=sr)
    res = json.lo

def put_diagnostic_report_request_id(diagnostic_report_id: str):
    response2 =  requests.put(fhirURL+"/DiagnosticReport/"+diagnostic_report_id)
    #  p.Patient.read('Patient/?expand=true', smart.server)
    res = json.loads(response2.text)
    return res
def set_ImagingStudy(sr):

    response2 =  requests.post(fhirURL+"/ImagingStudy", json=sr)
    res = json.loads(response2.text)
    return  res

def get_ImagingStudy():
    response2 =  requests.get(fhirURL+"/ImagingStudy")
    res = json.loads(response2.text)
    return res

def get_imaginstudy_id(id):
    response2 =  requests.get(fhirURL+"/ImagingStudy/"+id)
    res = json.loads(response2.text)
    return res


async def uploadFiles(files,ServiceRequest_id):
    print("uploading files for task  .....",ServiceRequest_id)
    url = OrthancURL + "/instances"
    print("url--->",url)
    response  = ""
    for file in files:
        
        data = await file.read()
        response2 =  requests.post(url,data=data, headers={'Content-Type': 'application/octet-stream'},verify=False)
        
        response  = response2.text
        

    # print(response)
    study = json.loads(response)
    print("orthanic response after image upload::",study)
    # Series = study["Series"]
    ParentPatient = study["ParentPatient"]
    
    ParentStudy = study["ParentStudy"]
    
    studies = orthanc.get_study(ParentStudy)
    # patient = json.loads(studies)
    patient = studies
    # print("studies ...",studies)
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
    
    try:
        study = {
            
            "referring_physician_name": ReferringPhysicianName,
            "study_id": ParentStudy,
            "study_instance_uid": StudyInstanceUID,
            "patient_name": PatientName,
            "patient_age": PatientBirthDate,
            "patient_sex": PatientSex,
            "patient_mrn":PatientID,
            "bodypart_examined": "Task",
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
    # print("Update db",study)
    # val = create_study(db,study)
    # print("before publish ....")

    sr2 = get_service_request_id(ServiceRequest_id)
    # print(sr2)
    structure_report = sr.ServiceRequest(sr2)
    # print(structure_report)
    structure_report = structure_report.as_json()
    # print("Structured report ::",structure_report)
    Note = structure_report["note"]
    Note = Note[0]
    body_site_code =  ""
    print(structure_report["bodySite"][0])
    try:
        # structure_report.bodySite
        body_site = structure_report["bodySite"][0]
        print(body_site)
        body_site = body_site["coding"]
        body_site_code = body_site[0]
        body_site_code =  body_site_code["code"]
    except Exception as e: 
        print("Exception::",str(e))
    # print(structure_report)
    imaging_study = imaging_s.ImagingStudy()
    imaging_study.status = "available"
    # modality = [
    #     {
    #     "system": "http://dicom.nema.org/resources/ontology/DCM",
    #     "code": "DX"
    #     }
    # ]
    # imaging_study.modality = modality

    structure_report['subject']
    subject =  {
        "reference": structure_report['subject']["reference"]
    }
    reference = ref.FHIRReference(subject)


    imaging_study.subject = reference
    now = datetime.now() # current date and time
    fhir_date2 = fhir_date.FHIRDate(now.strftime("%m/%d/%Y, %H:%M:%S"))
    # imaging_study.started =  fhir_date2
    basedOn = {
      "reference": "ServiceRequest/"+ ServiceRequest_id
      }
    reference = ref.FHIRReference(basedOn)
    imaging_study.basedOn = [reference]

    #  get referrer
    try:
        practitionar = structure_report['requester']["reference"]
        referer =  {
        "reference": practitionar
        }
        reference = ref.FHIRReference(referer)
        # practitionar = structure_report["requester"]
        print("practitionar ::",practitionar)
        imaging_study.referrer = reference
    except Exception as e: 
        print("Exception::",str(e))
    
    end_point = {
        "reference": "Endpoint/1"
        }
    reference = ref.FHIRReference(end_point)
    imaging_study.endpoint = [reference]

    
    imaging_study.numberOfSeries = 1
    imaging_study.numberOfSeries = 1

# # list for below
    # annot = fhir_annotation.Annotation("")
    # imaging_study.reasonCode = annot
    note2 = {
      "text": "XR Wrist 3+ Views"
    }
    annot = fhir_annotation.Annotation(Note)
    imaging_study.note = [annot]
    

    #  create series
    series = StudySeries()
    series.uid = StudyInstanceUID
    modality = {
        "system": "http://dicom.nema.org/resources/ontology/DCM",
        "code": "CT"
      }
    coding2 = coding.Coding(modality)
    series.modality =  coding2
    imaging_study.series = [series]

#     # imaging_study.series = ""
    print(imaging_study.as_json())
    response = set_ImagingStudy(imaging_study.as_json())
    # print(response)
    im_resp = imaging_s.ImagingStudy(response)
    im_resp = im_resp.id
    im_resp = im_resp
    # print(response)
    # print(structure_report)
    Task = ""
    if body_site_code == "27410004":
        Task = "ich"
    if body_site_code == "786838002":
        Task = "lung"
    if body_site_code == "thor":
        Task = "thor"
    if body_site_code == "Abdoman":
        Task = "Abdoman"
    if body_site_code == "totalseg":
        Task = "totalseg"
    
    if body_site_code == "93870000":
        Task = "liver"
    if body_site_code == "275978004":
        Task = "colon"
    if body_site_code == "432634008":
        Task = "breast_mri"

    # breast_fibro
    if body_site_code == "breast_fibro":
        Task = "breast_fibro"
    # 432634008
    
   
    red = redis.StrictRedis(redis_url,6379,password="m0nday",charset="utf-8",decode_responses=True)
    res = {
        "Task": Task,
        "pacs_url": OrthancURL,
        "api_url": apiURL,
        "ehr_url": fhir_url,
        "study_id": im_resp,
        "Series": Series,
        "ImagingStudy":im_resp,
        "patient_id": subject["reference"],
        "service_id": ServiceRequest_id,
        "ParentStudy": ParentStudy,
    }
    print("Task info ::",res)
    red.publish("test",json.dumps(res))
    print("after publish ....")
    print(subject)
    # res = json.loads(response)
    # print("Imaging is::",response['id'])
    return response
