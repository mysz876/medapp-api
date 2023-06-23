from typing import List
from application import db
from application.models.branch import Branch
from application.models.doctor import Doctor
from application.models.doctorExtra import DoctorExtra
from application.models.specialization import Specialization


def quDoctor() -> List[Doctor]:
    return db.session.query(Doctor).all()

def quDoctorById(id) -> Doctor:
    return db.session.query(Doctor)\
        .filter(Doctor.id == id)\
        .first()

def quDoctorWithExtra() -> List[DoctorExtra]:
    return db.session.query(Doctor, Branch, Specialization)\
        .join(Branch, Branch.id == Doctor.id_branch)\
        .join(Specialization, Specialization.id == Doctor.id_specialization)\
        .all()

def quDoctorByIdWithExtra() -> DoctorExtra:
    return db.session.query(Doctor, Branch, Specialization)\
        .join(Branch, Branch.id == Doctor.id_branch)\
        .join(Specialization, Specialization.id == Doctor.id_specialization)\
        .filter(Doctor.id == id)\
        .all()

def quDoctorOfBranch(idBranch) -> Doctor:
    return db.session.query(Doctor)\
        .filter(Doctor.id_branch == idBranch)\
        .first()

def quDoctorOfSpecialization(idSpecialization) -> Doctor:
    return db.session.query(Doctor)\
        .filter(Doctor.id_specialization == idSpecialization)\
        .first()

def quDoctorDelete() -> int:
    return db.session.query(Doctor)\
        .filter(Doctor.id == id)\
        .delete()
