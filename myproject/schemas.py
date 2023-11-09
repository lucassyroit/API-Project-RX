from pydantic import BaseModel


class DriverBase(BaseModel):
    first_name: str
    last_name: str
    country: str
    team: str
    active: bool


class DriverCreate(DriverBase):
    pass


class Driver(DriverBase):
    id: int

    class Config:
        orm_mode = True
