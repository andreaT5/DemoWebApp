import sqlite3
from flask import Flask, g
from flask_migrate import Migrate
from config import Config

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(Config.SQLALCHEMY_DATABASE_URI)
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def index():
    db = get_db()
    cursor = db.cursor()
    
    # Perform database operations
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    
    # Process the results or return them as JSON response
    # ...
    
    return "Hello, Flask!"