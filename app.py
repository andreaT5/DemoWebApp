from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from config import Config
from extension import db, jwt
from models.user import User
from db.database import get_db
import sqlite3

from routes.user import route_user
from routes.index import route_index


app = Flask(__name__)
app.debug = True
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt.init_app(app)
api = Api(app)

app.register_blueprint(route_user)
app.register_blueprint(route_index)

# conn = sqlite3.connect(Config.DBURL)
# cursor = conn.cursor()
# cursor.execute('select * from user')
# rows = cursor.fetchall()
# print(rows)
