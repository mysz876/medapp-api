from application.models.specialization import Specialization


def createSpecializationRow(data: dict):
    return Specialization(
        name = data.get('name')
    )

def updateSpecializationRow(specialization: Specialization, data: dict):
    specialization.name = data.get('name')
