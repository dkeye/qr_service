from typing import List
from uuid import uuid4

from sqlalchemy.orm import Session

from . import models, schemas
from .errors import DBNotFound, AppLogicException


def create_code(db: Session):
    db_item = models.Codes(code=str(uuid4()))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_code(db: Session, code: str) -> models.Codes:
    if db_code := db.query(models.Codes).filter(models.Codes.code == code).first():
        return db_code
    raise DBNotFound("Code not found")


def get_codes(db: Session) -> List[models.Codes]:
    return db.query(models.Codes).all()


def activate_code(db: Session, code: schemas.CodeBase) -> schemas.Code:
    db_item = get_code(db, code.code)
    if db_item.is_activated:
        raise AppLogicException("Code already activated")

    db_item.is_activated = True
    db.commit()
    db.refresh(db_item)

    return db_item


def switch(db: Session, code: str) -> schemas.Code:
    db_item = get_code(db, code)
    db_item.is_activated = not db_item.is_activated
    db.commit()
    db.refresh(db_item)

    return db_item


def delete_code(db: Session, code: str) -> None:
    db_item = get_code(db, code)
    db.delete(db_item)
    db.commit()


def clear_codes(db: Session) -> None:
    db.query(models.Codes).delete()
    db.commit()
