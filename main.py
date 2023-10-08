from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine, get_db
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

@app.get('/web-page/', response_model=list[schemas.WebPage])
def read_web_page_list(db: Session = Depends(get_db)):
    response = crud.get_web_page_list(db)
    return response

@app.post('/web-page/', response_model=schemas.WebPage)
def create_web_page(web_page: schemas.WebPageCreate, db: Session = Depends(get_db)):
    response = crud.post_web_page(db, web_page)
    return response