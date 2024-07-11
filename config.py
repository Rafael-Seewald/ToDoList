from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    task = db.Column(db.String(29), nullable=False)
    status = db.Column(db.Boolean, default=False)
