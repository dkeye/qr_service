from fastapi import Depends, APIRouter, Response, status
from sqlalchemy.orm import Session

from abstract_service import schemas, crud
from abstract_service.dependency import get_db
from abstract_service.security import get_token_header

router = APIRouter(
    dependencies=[Depends(get_token_header)],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "secret_token header invalid"}
    }
)


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schemas.Code)
def get_new_code(response: Response, db: Session = Depends(get_db)):
    response.status_code = status.HTTP_201_CREATED
    return crud.create_code(db)


@router.get(
    "/check/{code}",
    response_model=schemas.Code,
    responses={
        status.HTTP_200_OK: {"model": schemas.Code},
        status.HTTP_404_NOT_FOUND: {"description": "Code not found"},
    }
)
def check_code(code: str, db: Session = Depends(get_db)):
    return crud.get_code(db, code)


@router.post(
    "/activate",
    response_model=schemas.Code,
    responses={
        status.HTTP_200_OK: {"model": schemas.Code},
        status.HTTP_404_NOT_FOUND: {"description": "Code not found"},
        status.HTTP_406_NOT_ACCEPTABLE: {"description": "Code already activated"},
    }
)
def activate_code(code: schemas.CodeBase, db: Session = Depends(get_db)):
    result = crud.activate_code(db, code)
    return result
