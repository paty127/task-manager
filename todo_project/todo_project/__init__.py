from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
import logging
import sys
import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = '45cf93c4d41348cd9980674ade9a7356'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)

auth_logger = logging.getLogger('auth')
auth_logger.setLevel(logging.INFO)
_handler = logging.StreamHandler(sys.stdout)
_hostname = socket.gethostname()
_formatter = logging.Formatter('%(asctime)s ' + _hostname + ' task-manager[%(process)d]: %(levelname)s %(message)s')
_handler.setFormatter(_formatter)
auth_logger.addHandler(_handler)
auth_logger.propagate = False

@app.after_request
def set_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Resource-Policy'] = 'same-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    return response

from todo_project import routes

