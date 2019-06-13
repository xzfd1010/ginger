from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = RedPrint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_by_email():
    form = UserEmailForm(data=request.json).validate_for_api()
    # if form.validate():
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)
