from db import db
from entities.vehicle import Vehicle

class VehicleRepository:
    """Repositorio para operaciones CRUD sobre la entidad Vehicle."""

    def get_all(self):
        """Retorna todos los vehículos."""
        return Vehicle.query.all()

    def get_by_id(self, vehicle_id):
        """Retorna un vehículo por su ID, o None si no existe."""
        return Vehicle.query.get(vehicle_id)

    def create(self, vehicle_data):
        """
        Crea un vehículo.
        vehicle_data debe ser un diccionario con:
            - car_brand
            - arrival_location
            - applicant
        """
        vehicle = Vehicle(**vehicle_data)
        db.session.add(vehicle)
        db.session.commit()
        return vehicle

    def update(self, vehicle_id, vehicle_data):
        """
        Actualiza un vehículo existente.
        Retorna el vehículo actualizado o None si no existe.
        """
        vehicle = self.get_by_id(vehicle_id)
        if not vehicle:
            return None
        for key, value in vehicle_data.items():
            if hasattr(vehicle, key):
                setattr(vehicle, key, value)
        db.session.commit()
        return vehicle

    def delete(self, vehicle_id):
        """
        Elimina un vehículo por su ID.
        Retorna el vehículo eliminado o None si no existía.
        """
        vehicle = self.get_by_id(vehicle_id)
        if not vehicle:
            return None
        db.session.delete(vehicle)
        db.session.commit()
        return vehicle
