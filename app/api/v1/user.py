from app.libs.redprint import RedPrint
from app.libs.token_auth import auth

api = RedPrint('user')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    return 'a user'
