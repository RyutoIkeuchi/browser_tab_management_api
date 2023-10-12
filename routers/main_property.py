from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas, crud


router = APIRouter()

@router.get('/main_property/', response_model=list[schemas.MainProperty])
def read_main_property_list(db: Session = Depends(get_db)):
    response = crud.get_main_property_list(db)
    return response

@router.post('/main-property/', response_model=schemas.MainProperty)
def create_main_property(main_property: schemas.MainPropertyCreate, db: Session = Depends(get_db)):
    response = crud.post_main_property(db, main_property)
    return response