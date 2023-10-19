from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import (
    MetaData, Column, Integer, Float, Boolean, DateTime, func
)

from .database import Base


metadata = MetaData


class CadastreRequest(Base):
    __tablename__ = "cadastre_queries"

    metadata
    id = Column(Integer, primary_key=True, index=True)
    cadastre_number = Column(Integer, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    result = Column(Boolean, nullable=True)
    timestamp = Column(DateTime, default=func.now())


# class QueryResponse(BaseModel):
#     id: int
#     cadastre_number: int
#     latitude: float
#     longitude: float
#     response: bool
#     timestamp: datetime
    