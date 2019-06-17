from flask import jsonify
from sqlalchemy import or_

from app.libs.redprint import RedPrint
from app.models.book import Book
from app.validators.forms import BookSearchForm

api = RedPrint('book')


@api.route('')
def get_book():
    return 'a book'


@api.route('/search', methods=['GET', 'POST'])
def search_book():
    form = BookSearchForm().validate_for_api()
    print('form', form.data)
    q = form.q.data
    book = Book.query.filter(or_(Book.title.like(q), Book.publisher.like(q))).all()
    return jsonify(book)


# 获取书籍详情
@api.route('/<isbn>/detail')
def book_detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)
