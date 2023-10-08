from sqlalchemy.orm import Session
import database, models, schemas

def get_web_page_list(db: Session):
    return db.query(models.WebPage).all()

def post_web_page(db: Session, web_page: schemas.WebPageCreate):
    db_web_page = models.WebPage(web_page)
    db.add(db_web_page)
    db.commit()
    db.refresh(db_web_page)
    return db_web_page

def post_main_property(db: Session, main_property: schemas.MainPropertyCreate):
    db_main_property = models.MainProperty(name=main_property.name)
    db.add(db_main_property)
    db.commit()
    db.refresh(db_main_property)
    return db_main_property