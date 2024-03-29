from app.libs.error import APIException


class Success(APIException):
    code = 200
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 1


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


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'Forbidden'


class DuplicateGift(APIException):
    code = 400
    error_code = 2001
    msg = 'the current book has already in gift'
