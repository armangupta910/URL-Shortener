from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Text
from pydantic import BaseModel

Base = declarative_base()

class Short(Base):
    __tablename__ = "shorts"

    code = Column(String(12), primary_key=True)
    url = Column(Text, index=True)

class URLRequest(BaseModel):
    url: str