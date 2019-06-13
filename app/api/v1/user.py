from flask import jsonify

from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.user import User

api = RedPrint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    # 如何返回user？

    return jsonify(user)
