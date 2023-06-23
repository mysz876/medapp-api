from application import db
from application.models.doctor import Doctor

class Specialization(db.Model):
    __tablename__ = 'specialization'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode, nullable=False)

    rel_doctor = db.relationship(Doctor, backref='specialization')
