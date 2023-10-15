from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas.web_page as schemas
import crud


router = APIRouter()

@router.get('/web-page/', response_model=list[schemas.WebPage])
def read_web_page_list(db: Session = Depends(get_db)):
    response = crud.get_web_page_list(db)
    return response

@router.post('/web-page/', response_model=schemas.WebPage)
def create_web_page(web_page: schemas.WebPageCreate, db: Session = Depends(get_db)):
    response = crud.post_web_page(db, web_page)
    return response