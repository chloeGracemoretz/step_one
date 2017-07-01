from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def create_app():
	app=Flask(__name__)
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	return app