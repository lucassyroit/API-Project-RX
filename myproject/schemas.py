from pydantic import BaseModel


class DriverBase(BaseModel):
    first_name: str
    last_name: str
    country: str
    team: str
    is_active: bool


class DriverCreate(DriverBase):
    pass


class Driver(DriverBase):
    id: int

    class Config:
        orm_mode = True
