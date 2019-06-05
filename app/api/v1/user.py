from app.libs.redprint import RedPrint

api = RedPrint('user')


@api.route('/get')
def get_user():
    return 'a user'
