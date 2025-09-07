from app import db

class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Vehicle {self.brand} {self.model} ({self.year})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "make": self.brand,   
            "model": self.model,
            "year": self.year
        }
