from fastapi import Header, HTTPException

from abstract_service.settings import SECRET_TOKEN


async def get_token_header(secret_token: str = Header(...)):
    if secret_token != SECRET_TOKEN:
        raise HTTPException(status_code=400, detail="secret_token header invalid")
