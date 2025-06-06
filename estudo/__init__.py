from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'EEHJKWNWMKC8382DFJNFNJJ'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from estudo.views import homepage
from estudo.models import Contato