# vehicle_business.py
from repositories.vehicle_repository import VehicleRepository

class VehicleBusiness:
    """Capa de negocio para la gestión de vehículos."""

    def __init__(self):
        self.repo = VehicleRepository()

    def get_all_vehicles(self):
        """Retorna todos los vehículos."""
        return self.repo.get_all()

    def get_vehicle(self, vehicle_id):
        """Retorna un vehículo por su ID o None si no existe."""
        return self.repo.get_by_id(vehicle_id)

    def create_vehicle(self, vehicle_data):
        """
        Crea un vehículo.
        vehicle_data: dict validado por VehicleDTO con campos:
            - car_brand
            - arrival_location
            - applicant
        """
        return self.repo.create(vehicle_data)

    def update_vehicle(self, vehicle_id, vehicle_data):
        """
        Actualiza un vehículo existente.
        Retorna el vehículo actualizado o None si no existe.
        """
        existing_vehicle = self.repo.get_by_id(vehicle_id)
        if not existing_vehicle:
            return None
        return self.repo.update(vehicle_id, vehicle_data)

    def delete_vehicle(self, vehicle_id):
        """
        Elimina un vehículo por su ID.
        Retorna True si se eliminó, False si no existía.
        """
        vehicle = self.repo.get_by_id(vehicle_id)
        if not vehicle:
            return False
        self.repo.delete(vehicle_id)
        return True
