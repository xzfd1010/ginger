from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = RedPrint('client')


@api.route('/create', methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        # 个性化校验
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_by_email
        }
        # type转为enums类型了
        promise[form.data.type]()
    return 'a user'


def __register_by_email():
    form = UserEmailForm(data=request.json)
    if form.validata():
        User.register_by_email(form.nickname.data,
                               form.account.data,
                               form.secret.data)
