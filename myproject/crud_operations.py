from sqlalchemy.orm import Session

import models
import schemas


def get_drivers(db: Session):
    return db.query(models.Driver).all()


def get_driver(db: Session, driver_id: int):
    return db.query(models.Driver).filter(models.Driver.id == driver_id).first()


def create_driver(db: Session, driver: schemas.DriverCreate):
    db_driver = models.Driver(
        first_name=driver.first_name,
        last_name=driver.last_name,
        country=driver.country,
        team=driver.team,
        is_active=driver.is_active
    )
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def delete_driver(db: Session, driver_id: int):
    driver = db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    if driver is not None:
        db.delete(driver)
        db.commit()
        return True
    return False
