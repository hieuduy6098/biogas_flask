from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('biogas')

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:100998@localhost/biogas'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
