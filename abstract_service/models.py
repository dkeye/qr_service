from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class Codes(Base):
    __tablename__ = "codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    is_activated = Column(Boolean, default=False)
