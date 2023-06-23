from flask import Blueprint, request, jsonify

from application.services.branch_service import deleteBranch, getBranch, getBranches, newBranch, updateBranch

branch_bp = Blueprint("branch_bp", __name__)

@branch_bp.route("", methods=['POST', 'GET'])
def branch():
    if request.method == "POST":
        request_data = request.get_json()
        result = newBranch(request_data)
    if request.method == "GET":
        result = getBranches()
    return jsonify(result)

@branch_bp.route("/<id>", methods=['GET', 'PUT', 'DELETE'])
def branchId(id):
    id = int(id)
    if request.method == "GET":
        result = getBranch(id)
    if request.method == "PUT":
        request_data = request.get_json()
        result = updateBranch(id, request_data)
    if request.method == "DELETE":
        result = deleteBranch(id)
    return jsonify(result)
