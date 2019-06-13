from collections import namedtuple

from flask import g, current_app
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()

User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)

    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)  # data {id:'',type:''}
    except BadSignature:
        raise AuthFailed(msg='token is invalid')
    except SignatureExpired:
        raise AuthFailed(msg='token is expired')

    uid = data['uid']
    ac_type = data['type']
    return User(uid, ac_type, '')
