from turtle import pos
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# always move the variable in a config file and store these in env. variables as they should be not passed in source code
app.config['SECRET_KEY'] = 'faf63196a50f3ba09129c36ad595ceee'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# redirect to login page when user is /account is entered without logging in
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Registering the blueprint routes
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.errors.handlers import errors
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)
