from app.libs.error import APIException


class Success(APIException):
    code = 200
    msg = 'success'
    error_code = 0


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 999


class ServerError(APIException):
    code = 500
    msg = 'Sorry, we make a mistake'
    error_code = 999


class NotFound(APIException):
    code = 404
    msg = 'Cannot Find the user'
    error_code = 1008


class AuthFailed(APIException):
    code = 401
    msg = 'Unauthorized'
    error_code = 1009
