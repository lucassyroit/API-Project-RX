import os

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud
import models
import schemas
from database import engine, SessionLocal

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get all drivers
@app.get("/drivers/", response_model=List[schemas.Driver])
def read_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drivers = crud.get_drivers(db, skip=skip, limit=limit)
    return drivers


# Get a specific driver
@app.get("/drivers/{driver_id}", response_model=schemas.Driver)
def read_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = crud.get_driver(db, driver_id=driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver


# Create a new driver
@app.post("/drivers/", response_model=schemas.Driver)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    return crud.create_driver(db=db, driver=driver)


# Delete a driver
@app.delete("/drivers/{driver_id}")
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    if not crud.delete_driver(db, driver_id):
        raise HTTPException(status_code=404, detail="Driver not found")
    return {"detail": "Driver deleted"}






