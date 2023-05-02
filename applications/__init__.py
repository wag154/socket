from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
#connects to elephantsql, NOTE: MAKE SURE TO PUT `postgresql`, just postgres wont work!
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://:///lglgyiwg:PV7qSAUxQJ0qsZ-CgbzxbU7iriAlKkXc@horton.db.elephantsql.com/lglgyiwg'
app.config['SECRET_KEY'] = "pass"
#cors_allowed_origins to let all connections come for origin
socketio = SocketIO(app ,cors_allowed_origins="*")
db = SQLAlchemy(app)

from applications import route
