from application.models.doctor import Doctor
from application.models.doctorExtra import DoctorExtra


def mapDoctor(record: Doctor) -> dict:
    return {
        'id': record.id,
        'idBranch': record.id_branch,
        'idSpecialization': record.id_specialization,
        'name': record.name,
        'surname': record.surname,
        'dayCount': record.dayCount
    }

def mapDoctorExtra(record: DoctorExtra) -> dict:
    return {
        'id': record.Doctor.id,
        'idBranch': record.Branch.id,
        'nameBranch': record.Branch.name,
        'idSpecialization': record.Specialization.id,
        'nameSpecizalization': record.Specialization.name,
        'name': record.Doctor.name,
        'surname': record.Doctor.surname,
        'dayCount': record.Doctor.dayCount
    }
