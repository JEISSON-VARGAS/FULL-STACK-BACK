from app import db

class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_brand = db.Column(db.String(100), nullable=False)        # Marca del carro
    arrival_location = db.Column(db.String(100), nullable=False) # Localidad de llegada
    applicant = db.Column(db.String(100), nullable=False)        # Aspirante

    def __repr__(self):
        return f"<Vehicle {self.car_brand} {self.arrival_location} ({self.applicant})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "car_brand": self.car_brand,
            "arrival_location": self.arrival_location,
            "applicant": self.applicant
        }
