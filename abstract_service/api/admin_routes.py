from typing import List

from fastapi import Depends, APIRouter, Response, status
from sqlalchemy.orm import Session

from abstract_service import schemas, crud
from abstract_service.dependency import get_db
from abstract_service.security import get_token_header

router = APIRouter(
    prefix='/admin',
    dependencies=[Depends(get_token_header)],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "secret_token header invalid"}
    }
)


@router.post("/codes", response_model=List[schemas.Code])
def get_codes(db: Session = Depends(get_db)):
    return crud.get_codes(db)


@router.post(
    "/switch",
    response_model=schemas.Code,
    responses={
        status.HTTP_200_OK: {"model": schemas.Code},
        status.HTTP_404_NOT_FOUND: {"description": "Code not found"},
    }
)
def switch_code(code: schemas.CodeBase, db: Session = Depends(get_db)):
    return crud.switch(db, code.code)


@router.post(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {},
        status.HTTP_404_NOT_FOUND: {"description": "Code not found"},
        status.HTTP_406_NOT_ACCEPTABLE: {"description": "Code already activated"},
    }
)
def delete_code(code: schemas.CodeBase, response: Response, db: Session = Depends(get_db)):
    crud.delete_code(db, code.code)
    response.status_code = 204
    return
