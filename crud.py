from sqlalchemy.orm import Session
import database, models

def get_web_page_list(db: Session):
    return db.query(models.WebPage).all()