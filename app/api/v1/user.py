from app.libs.redprint import RedPrint

api = RedPrint('user')


@api.route('/', methods=['POST'])
def create_user():
    return 'a user'
