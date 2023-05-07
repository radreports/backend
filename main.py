from fastapi import FastAPI, Depends,Header
from starlette.requests import Request
import uvicorn

from app.api.api_v1.routers.users import users_router
from app.api.api_v1.routers.studies import studies_router
from app.api.api_v1.routers.ris import ris_router
from app.api.api_v1.routers.auth import auth_router
from app.core import config
from app.db.session import SessionLocal
from app.core.auth import get_current_active_user
# from app.core.celery_app import celery_app
# from app import tasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, Request, Depends, Response, encoders, File, UploadFile,BackgroundTasks, WebSocket
import typing as t
from typing import List, Optional,Union
from app.db.session import get_db
from app.db.crud import (
    get_studies,
   create_study,
    
)
from app.db.schemas import StudyCreate, StudyUpdate
app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)
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

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}

@app.post("/studies")
async def upload_files(files: List[UploadFile], background_tasks: BackgroundTasks,
userID: Union[str, None] = Header(default=None, convert_underscores=False)):
    print("inside upload_files")
    print("userID::",userID)
    print(len(files))
    # background_tasks.add_task(doWorkFlow,files,userID)
    
# @app.get("/api/v1/task")
# async def example_task():
#     celery_app.send_task("app.tasks.example_task", args=["Hello World"])

#     return {"message": "success"}

app.include_router(
    studies_router,
    prefix="/api/v1",
    tags=["users"],
    # dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    ris_router,
    prefix="/api/v1",
    tags=["users"],
    # dependencies=[Depends(get_current_active_user)],
)
# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
