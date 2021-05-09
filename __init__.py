from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# set up app + config
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'shopify'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024 # sum of file size < 20MB
app.config['UPLOAD_EXTENSIONS'] = ['jpg', 'png', 'gif'] # only images allowed
app.config['UPLOAD_PATH'] = 'uploads' # folder name to store photos

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
db.init_app(app)
# we need to initialize db first before using it in models.py
from .models import User 

# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))
