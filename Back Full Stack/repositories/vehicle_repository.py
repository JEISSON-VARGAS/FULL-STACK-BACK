# vehicle_repository.py
from db import db
from entities.vehicle import Vehicle

class VehicleRepository:
    def get_all(self):
        return Vehicle.query.all()

    def get_by_id(self, vehicle_id):
        return Vehicle.query.get(vehicle_id)

    def create(self, vehicle_data):
        vehicle = Vehicle(**vehicle_data)
        db.session.add(vehicle)
        db.session.commit()
        return vehicle

    def update(self, vehicle_id, vehicle_data):
        vehicle = self.get_by_id(vehicle_id)
        if vehicle:
            for key, value in vehicle_data.items():
                setattr(vehicle, key, value)
            db.session.commit()
        return vehicle

    def delete(self, vehicle_id):
        vehicle = self.get_by_id(vehicle_id)
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
        return vehicle
