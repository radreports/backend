from calendar import SATURDAY
from typing import List, Optional,Union

import uvicorn
from fastapi import FastAPI,Request,Header, Depends, Query, Body, File, UploadFile,BackgroundTasks, WebSocket
from pydantic import BaseModel, SecretStr

from fastapi_keycloak import FastAPIKeycloak, OIDCUser, UsernamePassword, HTTPMethod, KeycloakUser, KeycloakGroup

from beren import Orthanc
from fastapi.middleware.cors import CORSMiddleware

# from requests.auth import HTTPBasicAuth
import json

import InferenceService as inferService
from services import WorkflowService,database
from sse_starlette.sse import EventSourceResponse
from services.status_event_generator import status_event_generator,setStaus
from services import StatusQue
class Inference(BaseModel):
    bodyPart: str
    seriesID: str
    
class Flow(BaseModel):
    files: List[UploadFile]
        

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OrthancURL = "http://35.202.115.123:8042"
orthanc = Orthanc(OrthancURL)
# OrthancURL = "http://35.202.115.123:8042"
# auth = HTTPBasicAuth('demo', 'demo')
# orthanc = Orthanc(OrthancURL, auth=auth)

@app.get('/status/stream')
def runStatus(param1: str,request: Request):
    print("param1::",param1)
    event_generator = status_event_generator(request, param1)
    return EventSourceResponse(event_generator)


@app.get("/studies", tags=["Studies"])
def getStudies(userID: Union[str, None] = Header(default=None, convert_underscores=False)):
    print("User ID::",userID)
    studies = database.getStudies(userID)
    print(studies)
    queue = StatusQue.Singleton().getInstance()
    dummy = {userID: False}
    queue._Singleton__queue.update(dummy)
    return (studies)
   
@app.delete("/series/{seriesID}", status_code=204)
def delete_series(seriesID: str) -> None:
    print("delete",seriesID)
    orthanc.delete_series(seriesID)

def doProcess(seriesID,orthanc,OrthancURL,bodyPar):
    print("Waiing")
    print("opening")
    inferService.process(seriesID, orthanc,OrthancURL,bodyPar)

@app.post("/studies", tags=["Upload-Dicom"])
async def upload_files(files: List[UploadFile], background_tasks: BackgroundTasks,
userID: Union[str, None] = Header(default=None, convert_underscores=False)):
    print("inside upload_files")
    print("userID::",userID)
    print(len(files))
    # for file in files:
    #     print(file.filename)
    # userID = "Demo"

    queue = StatusQue.Singleton().getInstance()
    dummy = {userID: True}
    queue._Singleton__queue.update(dummy)
    # print(queue.__queue)
    # setStaus(True)
    # files = flow.files
    # background_tasks.add_task(doWorkFlow,files,userID)


if __name__ == '__main__':
    uvicorn.run('App:app', host="0.0.0.0", port=8081, reload=True)