from pydantic import BaseModel


class DriverBase(BaseModel):
    first_name: str
    last_name: str


class DriverCreate(DriverBase):
    country: str
    team: str

    class Config:
        orm_mode = True


class Driver(DriverBase):
    id: int
    country: str
    team: str

    class Config:
        orm_mode = True
