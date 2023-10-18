from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import (
    MetaData, Column, Integer, Float, Boolean, DateTime,
)

from .database import Base


metadata = MetaData


class Request(Base):
    __tablename__ = "queries"

    metadata
    id = Column(Integer, primary_key=True, index=True)
    cadastre_number = Column(Integer, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    response = Column(Boolean, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)


class QueryRequest(BaseModel):
    cadastre_number: int
    latitude: float
    longitude: float


class QueryResponse(BaseModel):
    result: bool
