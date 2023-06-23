from application.models.doctor import Doctor


def createDoctorRow(data: dict):
    return Doctor(
        name = data.get('name'),
        surname = data.get('surname'),
        dayCount = data.get('dayCount'),
        id_branch = data.get('idBranch'),
        id_specialization = data.get('idSpecialization'),
    )

def updateDoctorRow(doctor: Doctor, data: dict):
    doctor.name = data.get('name')
    doctor.surname = data.get('surname')
    doctor.dayCount = data.get('dayCount')
