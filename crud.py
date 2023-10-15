from sqlalchemy.orm import Session
import database, models
from schemas import web_page, main_property, sub_property

def get_web_page_list(db: Session):
    return db.query(models.WebPage).all()

def post_web_page(db: Session, web_page: web_page.WebPageCreate):
    db_web_page = models.WebPage(web_page)
    db.add(db_web_page)
    db.commit()
    db.refresh(db_web_page)
    return db_web_page

def get_main_property_list(db: Session):
    return db.query(models.MainProperty).all()

def post_main_property(db: Session, main_property: main_property.MainPropertyCreate):
    db_main_property = models.MainProperty(name=main_property.name)
    db.add(db_main_property)
    db.commit()
    db.refresh(db_main_property)
    return db_main_property

def get_sub_property_list(db: Session):
    return db.query(models.SubProperty).all()

def post_sub_property(db: Session, sub_property: sub_property.SubPropertyCreate):
    db_sub_property = models.SubProperty(name=sub_property.name, main_property_id=sub_property.main_property_id)
    db.add(db_sub_property)
    db.commit()
    db.refresh(db_sub_property)
    return db_sub_property