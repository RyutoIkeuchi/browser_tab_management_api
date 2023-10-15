from pydantic import BaseModel        
from typing import Union

class SubPropertyBase(BaseModel):
    name: str
    main_property_id: int
    
class SubPropertyCreate(SubPropertyBase):
    pass
    
class SubProperty(SubPropertyBase):
    id: int
    
    class Config:
        orm_mode = True
