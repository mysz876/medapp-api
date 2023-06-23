from application import db
from application.models.doctor import Doctor

class Branch(db.Model):
    __tablename__ = 'branch'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode, nullable=False)

    rel_doctor = db.relationship(Doctor, backref='branch')
