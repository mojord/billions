from os import getenv
from app import app
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///apietila"
db = SQLAlchemy(app)
