from app.libs.redprint import RedPrint

api = RedPrint('book')


@api.route('')
def get_book():
    return 'a book'
