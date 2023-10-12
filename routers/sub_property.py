from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas, crud


router = APIRouter()

@router.post('/sub-property/', response_model=schemas.SubProperty)
def create_sub_property(sub_property: schemas.SubPropertyCreate, db: Session = Depends(get_db)):
    response = crud.post_sub_property(db, sub_property)
    return response