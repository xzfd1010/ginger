'''
flask核心对象相关的操作
'''
from flask import Flask

from app.api.v1 import register_redprint


def register_blueprints(app):
    bp_v1 = register_redprint()
    app.register_blueprint(bp_v1, url_prefix='/v1')
    # app.register_blueprint(user.user)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    return app
