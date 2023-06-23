from application.models.branch import Branch

def mapBranch(record: Branch) -> dict:
    return {
        'id': record.id,
        'name': record.name
    }
