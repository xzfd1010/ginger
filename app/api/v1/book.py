from app.libs.redprint import RedPrint

api = RedPrint('book')


@api.route('/get')
def get_book():
    return 'a book'
