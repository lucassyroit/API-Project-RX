from sqlalchemy import Column, Integer, String

from database import Base


class Driver(Base):
    __tablename__ = "driver"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    country = Column(String, index=True)
    team = Column(String, index=True)
