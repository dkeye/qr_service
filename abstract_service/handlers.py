from fastapi.exception_handlers import http_exception_handler


async def app_logic_exception_handler(request, exc):
    return await http_exception_handler(request, exc)
