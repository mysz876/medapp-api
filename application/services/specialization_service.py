from typing import List
from application import db
from application.functions.specialization_function import createSpecializationRow, updateSpecializationRow
from application.mappers.specialization_mapper import mapSpecialization
from application.queries.doctor_query import quDoctorOfSpecialization
from application.queries.specialization_query import quSpecialization, quSpecializationById, quSpecializationDelete, quSpecializationIsUnique

def getSpecializations() -> List[dict]:
    specializations = quSpecialization()
    result = []
    for specialization in specializations:
        result.append(mapSpecialization(specialization))
    return result

def getSpecialization(id) -> dict:
    specialization = quSpecializationById(id)
    return mapSpecialization(specialization)

def newSpecialization(data: dict) -> dict:
    unique = quSpecializationIsUnique(data['name'])
    if unique:
        return { 'result': False, 'msg': 'Istnieje oddział o takiej nazwie. Nie utworozno oddziału'}
    newSpecialization = createSpecializationRow(data)
    db.session.add(newSpecialization)
    db.session.commit()
    return { 'result': True, 'msg': 'Dodano nowy dział'}

def updateSpecialization(id: int, data: dict) -> dict:
    unique = quSpecializationIsUnique(data['name'])
    if unique and unique.id != id:
        return { 'result': False, 'msg': 'Istnieje oddział o takiej nazwie. Dane niezaktualizowane'}
    specialization = quSpecializationById(id)
    updateSpecializationRow(specialization, data)
    db.session.commit()
    return { 'result': True, 'msg': 'Dane oddziału zaktualizowane pomyślnie'}

def deleteSpecialization(id) -> dict:
    if quDoctorOfSpecialization(id):
        return { 'result': False, 'msg': 'Nie mozna usunąc specjalizacji do której przypisany jest lekarz'}
    quSpecializationDelete()
    db.session.commit()
    return { 'result': True, 'msg': 'Usunięto dział'}
