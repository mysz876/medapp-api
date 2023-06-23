from flask import Blueprint, request, jsonify

from application.services.doctor_service import deleteDoctor, getDoctor, getDoctors, newDoctor, updateDoctor

doctor_bp = Blueprint("doctor_bp", __name__)

@doctor_bp.route("", methods=['POST', 'GET'])
def doctor():
    if request.method == "POST":
        request_data = request.get_json()
        result = newDoctor(request_data)
    if request.method == "GET":
        result = getDoctors()
    return jsonify(result)

@doctor_bp.route("/<id>", methods=['GET', 'PUT', 'DELETE'])
def doctorId(id):
    if request.method == "GET":
        result = getDoctor(id)
    if request.method == "PUT":
        request_data = request.get_json()
        result = updateDoctor(id, request_data)
    if request.method == "DELETE":
        result = deleteDoctor(id)
    return jsonify(result)
