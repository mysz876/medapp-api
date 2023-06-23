from application import db

class Doctor(db.Model):
    __tablename__ = "doctor"
    id = db.Column('id', db.Integer, primary_key = True)
    id_branch = db.Column('id_branch', db.Integer, db.ForeignKey('branch.id'), nullable=False)
    id_specialization = db.Column('id_specialization', db.Integer, db.ForeignKey('specialization.id'), nullable=False)
    name = db.Column('name', db.Unicode, nullable=False)
    surname = db.Column('surname', db.Unicode, nullable=False)
    dayCount = db.Column('day_count', db.Integer, nullable=False)
