from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from abstract_service import schemas, crud
from abstract_service.dependency import get_db
from abstract_service.security import get_token_header

router = APIRouter(
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "secret_token header invalid"}
    }
)


@router.post("/create/", response_model=schemas.Code)
def get_new_code(db: Session = Depends(get_db)):
    return crud.create_code(db)


@router.get(
    "/check/{code}",
    response_model=schemas.Code,
    responses={
        200: {"model": schemas.Code},
        404: {"description": "Code not found"},
    }
)
def check_code(code: str, db: Session = Depends(get_db)):
    return crud.get_code(db, code)


@router.post(
    "/activate",
    response_model=schemas.Code,
    responses={
        200: {"model": schemas.Code},
        404: {"description": "Code not found"},
        406: {"description": "Code already activated"},
    }
)
def activate_code(code: schemas.CodeBase, db: Session = Depends(get_db)):
    result = crud.activate_code(db, code)
    return result
