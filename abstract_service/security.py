from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader

from abstract_service.settings import get_settings

oauth2_scheme = APIKeyHeader(name='secret_token')


async def get_token_header(secret_token: str = Depends(oauth2_scheme)):
    if secret_token != get_settings().secret_token:
        raise HTTPException(status_code=401, detail="secret_token header invalid")
