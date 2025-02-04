# Imports
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import os
import crud_operations
import models
import schemas
from database import SessionLocal, engine
from typing import List

# Database Initialization
if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')
models.Base.metadata.create_all(bind=engine)

# FastAPI App Setup
app = FastAPI()

# CORS Middleware Configuration:
origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500/",
    "http//lucassyroit.github.io/",
    "https://lucassyroit.github.io/",
    "https://lucassyroit.github.io/API-Project-RX-frontend/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get all drivers
@app.get("/drivers/", response_model=List[schemas.Driver])
def get_all_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drivers = crud_operations.get_drivers(db, skip=skip, limit=limit)
    return drivers


# Get a specific driver
@app.get("/drivers/{driver_id}", response_model=schemas.Driver)
def get_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = crud_operations.get_driver(db, driver_id=driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver


# Create a new driver
@app.post("/createDriver/", response_model=schemas.Driver)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    return crud_operations.create_driver(db=db, driver=driver)


# Delete a driver
@app.delete("/deleteDriver/{driver_id}")
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    if not crud_operations.delete_driver(db, driver_id):
        raise HTTPException(status_code=404, detail="Driver not found")
    return {"detail": "Driver deleted"}
