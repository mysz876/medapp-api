from typing import List
from application import db
from application.models.branch import Branch
from sqlalchemy import func

def quBranch() -> List[Branch]:
    return db.session.query(Branch).all()

def quBranchById(id) -> Branch:
    return db.session.query(Branch)\
        .filter(Branch.id == id)\
        .first()

def quBranchIsUnique(name) -> Branch:
    return db.session.query(Branch)\
        .filter(func.lower(name) == func.lower(Branch.name))\
        .first()

def quBranchDelete(id) -> int:
    db.session.query(Branch)\
        .filter(Branch.id == id)\
        .delete()
