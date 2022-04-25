from app import db

from sqlalchemy import ForeignKey


# User ORM for SQLAlchemy
class UniqueIDs(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    uuid = db.Column(db.String(100), nullable = False, unique = True)
    useragent = db.Column(db.String(200), nullable = False)