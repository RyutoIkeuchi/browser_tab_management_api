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