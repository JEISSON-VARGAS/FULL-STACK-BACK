# vehicle_business.py
from repositories.vehicle_repository import VehicleRepository

class VehicleBusiness:
    def __init__(self):
        self.repo = VehicleRepository()

    def get_all_vehicles(self):
        return self.repo.get_all()

    def get_vehicle(self, vehicle_id):
        return self.repo.get_by_id(vehicle_id)

    def create_vehicle(self, vehicle_data):
        return self.repo.create(vehicle_data)

    def update_vehicle(self, vehicle_id, vehicle_data):
        return self.repo.update(vehicle_id, vehicle_data)

    def delete_vehicle(self, vehicle_id):
        return self.repo.delete(vehicle_id)
