from flask import Flask
from flask_cors import CORS
from settings.configuration import Config
from ext import register_extensions
from information_cpu.views import information_cpu


def create_application():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(Config)
    register_extensions(app)

    app.register_blueprint(information_cpu, url_prefix='/information_cpu')
    return app
