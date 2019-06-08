'''
flask核心对象相关的操作
'''
from flask import Flask, current_app

from app.api.v1 import register_redprint


def register_blueprints(app):
    bp_v1 = register_redprint()
    app.register_blueprint(bp_v1, url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        # print(current_app)
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprints(app)
    register_plugin(app)

    return app
