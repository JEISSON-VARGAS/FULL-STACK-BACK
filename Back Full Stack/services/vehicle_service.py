# vehicle_service.py
from repositories.vehicle_repository import VehicleRepository
from entities.vehicle import Vehicle

class VehicleService:
    """Capa de servicio para manejar la lógica de vehículos."""

    def __init__(self):
        self.repo = VehicleRepository()

    def get_all_vehicles(self):
        """Retorna todos los vehículos."""
        return self.repo.get_all()

    def get_vehicle_by_id(self, vehicle_id):
        """Retorna un vehículo por ID o lanza un error si no existe."""
        vehicle = self.repo.get_by_id(vehicle_id)
        if not vehicle:
            raise ValueError(f"Vehículo con ID {vehicle_id} no encontrado")
        return vehicle

    def create_vehicle(self, data):
        """
        Crea un nuevo vehículo.
        data debe contener:
            - car_brand
            - arrival_location
            - applicant
        """
        # Aquí se podrían agregar validaciones adicionales de seguridad
        vehicle = Vehicle(**data)
        return self.repo.create(data)

    def update_vehicle(self, vehicle_id, data):
        """
        Actualiza un vehículo existente.
        Lanza error si el vehículo no existe.
        """
        vehicle = self.repo.get_by_id(vehicle_id)
        if not vehicle:
            raise ValueError(f"Vehículo con ID {vehicle_id} no encontrado")

        for key, value in data.items():
            if hasattr(vehicle, key):
                setattr(vehicle, key, value)
        
        # Commit de los cambios
        self.repo.update(vehicle_id, data)
        return vehicle

    def delete_vehicle(self, vehicle_id):
        """
        Elimina un vehículo por ID.
        Lanza error si no existe.
        """
        vehicle = self.repo.get_by_id(vehicle_id)
        if not vehicle:
            raise ValueError(f"Vehículo con ID {vehicle_id} no encontrado")
        self.repo.delete(vehicle_id)
        return True
