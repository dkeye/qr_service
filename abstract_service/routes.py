from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from abstract_service import schemas, crud
from abstract_service.dependency import get_db

router = APIRouter()


@router.post("/create/", response_model=schemas.Code)
def create_code(db: Session = Depends(get_db)):
    return crud.create_code(db)


@router.get("/check/{code}", response_model=schemas.Code)
def get_code(code: str, db: Session = Depends(get_db)):
    db_code = crud.get_code(db, code)
    if db_code is None:
        raise HTTPException(status_code=404, detail="Code not found")
    return db_code


@router.post("/activate", response_model=schemas.Code)
def activate_code(code: schemas.CodeBase, db: Session = Depends(get_db)):
    result = crud.activate_code(db, code)
    return result
