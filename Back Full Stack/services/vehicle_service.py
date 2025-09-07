from repositories.vehicle_repository import VehicleRepository
from entities.vehicle import Vehicle

class VehicleService:

    @staticmethod
    def get_all_vehicles():
        return VehicleRepository.get_all()

    @staticmethod
    def get_vehicle_by_id(vehicle_id):
        vehicle = VehicleRepository.get_by_id(vehicle_id)
        if not vehicle:
            raise ValueError(f"Vehicle with id {vehicle_id} not found")
        return vehicle

    @staticmethod
    def create_vehicle(data):
        # data llega como diccionario desde el DTO
        vehicle = Vehicle(**data)
        return VehicleRepository.save(vehicle)

    @staticmethod
    def update_vehicle(vehicle_id, data):
        vehicle = VehicleRepository.get_by_id(vehicle_id)
        if not vehicle:
            raise ValueError(f"Vehicle with id {vehicle_id} not found")

        for key, value in data.items():
            setattr(vehicle, key, value)

        VehicleRepository.update()
        return vehicle

    @staticmethod
    def delete_vehicle(vehicle_id):
        vehicle = VehicleRepository.get_by_id(vehicle_id)
        if not vehicle:
            raise ValueError(f"Vehicle with id {vehicle_id} not found")

        VehicleRepository.delete(vehicle)
        return True
