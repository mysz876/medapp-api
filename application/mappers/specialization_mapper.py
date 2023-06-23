from application.models.specialization import Specialization


def mapSpecialization(record: Specialization) -> dict:
    return {
        'id': record.id,
        'name': record.name
    }
