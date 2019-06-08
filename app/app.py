'''
flask核心对象相关的操作
'''
from flask import Flask

from app.api.v1 import register_redprint
from app.models.base import db


def register_blueprints(app):
    bp_v1 = register_redprint()
    app.register_blueprint(bp_v1, url_prefix='/v1')


def register_plugins(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    register_plugins(app)
    return app
