from pydantic import BaseModel        
from typing import Union
from schemas.web_page import WebPage
from schemas.sub_property import SubProperty

class MainPropertyBase(BaseModel):
    name: str
    
class MainPropertyCreate(MainPropertyBase):
    pass

class MainProperty(MainPropertyBase):
    id: int
    web_page_list: list[WebPage] = []
    sub_property_list: list[SubProperty] = []
    
    class Config:
        orm_mode = True