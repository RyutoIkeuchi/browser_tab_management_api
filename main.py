from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine, get_db
import models, schemas, crud
from routers import main_property, web_page, sub_property

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(web_page.router)
app.include_router(main_property.router)
app.include_router(sub_property.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def read_root():
    return {"Hello": "World"}