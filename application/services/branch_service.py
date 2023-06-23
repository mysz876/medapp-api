from typing import List
from application.functions.branch_function import createBranchRow, updateBranchRow
from application.mappers.branch_mapper import mapBranch
from application.queries.branch_query import quBranch, quBranchById, quBranchDelete, quBranchIsUnique
from application import db
from application.queries.doctor_query import quDoctorOfBranch

def getBranches() -> List[dict]:
    branches = quBranch()
    result = []
    for branch in branches:
        result.append(mapBranch(branch))
    return result

def getBranch(id) -> dict:
    branch = quBranchById(id)
    return mapBranch(branch)

def newBranch(data: dict) -> dict:
    unique = quBranchIsUnique(data['name'])
    if unique:
        return { 'result': False, 'msg': 'Istnieje oddział o takiej nazwie. Nie utworozno oddziału'}
    newBranch = createBranchRow(data)
    db.session.add(newBranch)
    db.session.commit()
    return { 'result': True, 'msg': 'Dodano nowy oddział'}

def updateBranch(id: int, data: dict) -> dict:
    unique = quBranchIsUnique(data['name'])
    if unique and unique.id != id:
        return { 'result': False, 'msg': 'Istnieje oddział o takiej nazwie. Dane niezaktualizowane'}
    branch = quBranchById(id)
    updateBranchRow(branch, data)
    db.session.commit()
    return { 'result': True, 'msg': 'Dane oddziału zaktualizowane pomyślnie'}

def deleteBranch(id) -> dict:
    if quDoctorOfBranch(id):
        return { 'result': False, 'msg': 'Nie mozna usunąc oddziału do którego przypisany jest lekarz'}
    quBranchDelete(id)
    db.session.commit()
    return { 'result': True, 'msg': 'Usunięto oddział'}
