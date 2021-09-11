from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from abstract_service.settings import SECRET_TOKEN


class SecretTokenMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.headers.get("secretToken") != SECRET_TOKEN:
            return JSONResponse(status_code=401)
        response = await call_next(request)
        return response
