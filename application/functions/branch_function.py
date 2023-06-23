from application.models.branch import Branch


def createBranchRow(data: dict):
    return Branch(
        name = data.get('name')
    )

def updateBranchRow(branch: Branch, data: dict):
    branch.name = data.get('name')
