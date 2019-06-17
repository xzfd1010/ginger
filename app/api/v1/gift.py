from flask import g

from app.libs.error_code import DuplicateGift, Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.book import Book
from app.models.gift import Gift

api = RedPrint('gift')


@api.route('/<isbn>', methods=['POST'])
@auth.login_required
def create(isbn):
    uid = g.user.uid
    with db.auto_commit():
        Book.query.filter_by(isbn=isbn).first_or_404()  # 检测书籍是否存在
        gift = Gift.query.filter_by(isbn=isbn, uid=uid).first()  # 检测礼物是否已经存在
        if gift:
            raise DuplicateGift()
        gift = Gift()
        gift.isbn = isbn
        gift.uid = uid
        db.session.add(gift)
    return Success()
