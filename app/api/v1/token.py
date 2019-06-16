from app.libs.enums import ClientTypeEnum
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import ClientForm

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from flask import current_app as app, jsonify

api = RedPrint('token')


@api.route('', methods=['POST'])
def get_token():
    '''
    校验用户名密码，返回用户对应token
    '''

    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }

    identity = promise[form.type.data](form.account.data, form.secret.data)

    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'],
                                expiration=app.config['TOKEN_EXPIRATION'])

    t = {
        'token': token.decode('ascii')
    }

    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    # scope写入令牌
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })
