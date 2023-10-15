from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas.sub_property as schemas
import crud


router = APIRouter()

@router.get('/sub_property/', response_model=list[schemas.SubProperty])
def read_sub_property_list(db: Session = Depends(get_db)):
    response = crud.get_sub_property_list(db)
    return response

@router.post('/sub-property/', response_model=schemas.SubProperty)
def create_sub_property(sub_property: schemas.SubPropertyCreate, db: Session = Depends(get_db)):
    response = crud.post_sub_property(db, sub_property)
    return response