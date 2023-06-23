from typing import List
from application.functions.doctor_function import createDoctorRow, updateDoctorRow
from application.mappers.doctor_mapper import mapDoctorExtra
from application import db
from application.queries.doctor_query import quDoctorById, quDoctorByIdWithExtra, quDoctorDelete, quDoctorWithExtra


def getDoctors() -> List[dict]:
    doctors = quDoctorWithExtra()
    result = []
    for doctor in doctors:
        result.append(mapDoctorExtra(doctor))
    return result

def getDoctor(id) -> dict:
    return mapDoctorExtra(quDoctorByIdWithExtra(id))

def deleteDoctor(id) -> dict:
    quDoctorDelete(id)
    db.session.commit()
    return { 'result': True, 'msg': 'Usunieto lekarza'}

def newDoctor(data) -> dict:
    doctor = createDoctorRow(data)
    db.session.add(doctor)
    db.session.commit()
    return { 'result': True, 'msg': 'Pomyślnie utworzono lekarza'}

def updateDoctor(id, data) -> dict:
    doctor = quDoctorById(id)
    updateDoctorRow(doctor, data)
    db.session.commit()
    return { 'result': True, 'msg': 'Pomyślnie zaktualizowano lekarza'}
