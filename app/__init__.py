from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

UPLOAD_FOLDER= "./app/static/uploads"
app.config['SECRET_KEY'] = "aaa"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:123456qa@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
