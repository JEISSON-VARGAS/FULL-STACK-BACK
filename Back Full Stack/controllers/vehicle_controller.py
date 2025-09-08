# vehicle_controller.py
from flask import Blueprint, request, jsonify
from business.vehicle_business import VehicleBusiness
from dtos.vehicle_dto import VehicleDTO
from marshmallow import ValidationError # type: ignore

vehicle_bp = Blueprint("vehicle_bp", __name__)
business = VehicleBusiness()
vehicle_schema = VehicleDTO()

@vehicle_bp.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = business.get_all_vehicles()
    return jsonify([v.to_dict() for v in vehicles])

@vehicle_bp.route("/vehicles/<int:vehicle_id>", methods=["GET"])
def get_vehicle(vehicle_id):
    vehicle = business.get_vehicle(vehicle_id)
    if vehicle:
        return jsonify(vehicle.to_dict())
    return {"message": "Vehículo no encontrado"}, 404

@vehicle_bp.route("/vehicles", methods=["POST"])
def create_vehicle():
    data = request.get_json()
    try:
        # Validar datos con DTO
        validated_data = vehicle_schema.load(data)
    except ValidationError as err:
        return {"errors": err.messages}, 400

    vehicle = business.create_vehicle(validated_data)
    return jsonify(vehicle.to_dict()), 201

@vehicle_bp.route("/vehicles/<int:vehicle_id>", methods=["PUT"])
def update_vehicle(vehicle_id):
    data = request.get_json()
    try:
        validated_data = vehicle_schema.load(data)
    except ValidationError as err:
        return {"errors": err.messages}, 400

    vehicle = business.update_vehicle(vehicle_id, validated_data)
    if vehicle:
        return jsonify(vehicle.to_dict())
    return {"message": "Vehículo no encontrado"}, 404

@vehicle_bp.route("/vehicles/<int:vehicle_id>", methods=["DELETE"])
def delete_vehicle(vehicle_id):
    vehicle = business.delete_vehicle(vehicle_id)
    if vehicle:
        return {"message": "Vehículo eliminado"}
    return {"message": "Vehículo no encontrado"}, 404
