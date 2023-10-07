from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class WebPage(Base):
    __tablename__ = 'web_pages'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    image = Column(String, nullable=True)
    url = Column(String)
    main_property_id = Column(Integer, ForeignKey('main_properties.id'))
    sub_property_list = relationship('WebPageSubProperty', backref='web_pages')
    
class WebPageSubProperty(Base):
    __tablename__ = 'web_page_sub_properties'
    id = Column(Integer, primary_key=True)
    web_page_id = Column(Integer, ForeignKey('web_pages.id'))
    sub_property_id = Column(Integer, ForeignKey('sub_properties.id'))
    

class MainProperty(Base):
    __tablename__ = 'main_properties'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    web_page_list = relationship('WebPage', backref='main_properties')
    sub_property_list = relationship('SubProperty', backref='main_properties')
    
class SubProperty(Base):
    __tablename__ = 'sub_properties'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    main_property_id = Column(Integer, ForeignKey('main_properties.id'))
    