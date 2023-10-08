from pydantic import BaseModel        
from typing import Union

class SubPropertyBase(BaseModel):
    name: str
    main_property_id: int
    
class SubProperty(SubPropertyBase):
    id: int
    
    class Config:
        orm_mode = True
        
        
class WebPageBase(BaseModel):
    title: str
    description: str
    image: Union[str, None] = None
    url: str
    main_property_id: int

class WebPageCreate(WebPageBase):
    sub_property_id_list: list[int] = []

class WebPage(WebPageBase):
    id: int
    sub_property_list: list[SubProperty] = []
    class Config:
        orm_mode = True

class WebPageSubPropertyBase(BaseModel):
    web_page_id: int
    sub_property_id: int
    
class WebPageSubProperty(WebPageSubPropertyBase):
    id: int
    
    class Config:
        orm_mode = True
        

class MainPropertyBase(BaseModel):
    name: str
    web_page_list: list[WebPage] = []
    sub_property_list: list[SubProperty] = []

class MainProperty(MainPropertyBase):
    id: int
    
    class Config:
        orm_mode = True