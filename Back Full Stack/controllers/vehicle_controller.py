# vehicle_controller.py
from flask import Blueprint, request, jsonify
from business.vehicle_business import VehicleBusiness

vehicle_bp = Blueprint("vehicle_bp", __name__)
business = VehicleBusiness()

@vehicle_bp.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = business.get_all_vehicles()
    return jsonify([v.to_dict() for v in vehicles])  # Asegúrate que tu entidad tenga un método `to_dict()`

@vehicle_bp.route("/vehicles/<int:vehicle_id>", methods=["GET"])
def get_vehicle(vehicle_id):
    vehicle = business.get_vehicle(vehicle_id)
    if vehicle:
        return jsonify(vehicle.to_dict())
    return {"message": "Vehicle not found"}, 404

@vehicle_bp.route("/vehicles", methods=["POST"])
def create_vehicle():
    data = request.get_json()
    vehicle = business.create_vehicle(data)
    return jsonify(vehicle.to_dict()), 201

@vehicle_bp.route("/vehicles/<int:vehicle_id>", methods=["PUT"])
def update_vehicle(vehicle_id):
    data = request.get_json()
    vehicle = business.update_vehicle(vehicle_id, data)
    if vehicle:
        return jsonify(vehicle.to_dict())
    return {"message": "Vehicle not found"}, 404

@vehicle_bp.route("/vehicles/<int:vehicle_id>", methods=["DELETE"])
def delete_vehicle(vehicle_id):
    vehicle = business.delete_vehicle(vehicle_id)
    if vehicle:
        return {"message": "Vehicle deleted"}
    return {"message": "Vehicle not found"}, 404
