from fastapi import Header, HTTPException

from abstract_service.settings import get_settings


async def get_token_header(secret_token: str = Header(...)):
    if secret_token != get_settings().secret_token:
        raise HTTPException(status_code=401, detail="secret_token header invalid")
