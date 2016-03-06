__author__ = 'Cloud'
from flask import Flask
from config import config

app = Flask(__name__)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .base import bp

    app.register_blueprint(bp)

    app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

    return app


def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)
