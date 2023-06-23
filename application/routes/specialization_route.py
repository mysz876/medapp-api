from flask import Blueprint, request, jsonify

from application.services.specialization_service import deleteSpecialization, getSpecialization, getSpecializations, newSpecialization, updateSpecialization

specialization_bp = Blueprint("specialization_bp", __name__)

@specialization_bp.route("", methods=['POST', 'GET'])
def specialization():
    if request.method == "POST":
        request_data = request.get_json()
        result = newSpecialization(request_data)
    if request.method == "GET":
        result = getSpecializations()
    return jsonify(result)

@specialization_bp.route("/<id>", methods=['GET', 'PUT', 'DELETE'])
def specializationId(id):
    if request.method == "GET":
        result = getSpecialization(id)
    if request.method == "PUT":
        request_data = request.get_json()
        result = updateSpecialization(id, request_data)
    if request.method == "DELETE":
        result = deleteSpecialization(id)
    return jsonify(result)
