from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND


class AppLogicException(Exception):
    def __init__(self, detail):
        self.detail = detail

    status_code = HTTP_400_BAD_REQUEST
    pass


class DBNotFound(AppLogicException):
    status_code = HTTP_404_NOT_FOUND
    pass
