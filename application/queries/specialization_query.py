from typing import List
from application import db
from application.models.specialization import Specialization
from sqlalchemy import func

def quSpecialization() -> List[Specialization]:
    return db.session.query(Specialization).all()

def quSpecializationById(id) -> Specialization:
    return db.session.query(Specialization)\
        .filter(Specialization.id == id)\
        .first()

def quSpecializationIsUnique(name) -> Specialization:
    return db.session.query(Specialization)\
        .filter(func.lower(name) == func.lower(Specialization.name))\
        .first()

def quSpecializationDelete(id) -> int:
    db.session.query(Specialization)\
        .filter(Specialization.id == id)\
        .delete()
