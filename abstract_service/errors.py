from starlette.status import HTTP_404_NOT_FOUND, HTTP_406_NOT_ACCEPTABLE


class AppLogicException(Exception):
    def __init__(self, detail):
        self.detail = detail

    status_code = HTTP_406_NOT_ACCEPTABLE


class DBNotFound(AppLogicException):
    status_code = HTTP_404_NOT_FOUND
