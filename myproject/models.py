from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class Driver(Base):
    __tablename__ = "driver"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    country = Column(String, index=True, default="Unknown")
    team = Column(String, index=True, default="none")
    is_active = Column(Boolean, index=True, default=True)
