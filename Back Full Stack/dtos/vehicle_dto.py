from marshmallow import Schema, fields # pyright: ignore[reportMissingImports]

class VehicleDTO(Schema):
    id = fields.Int(dump_only=True)   # Solo para respuestas, no para crear
    brand = fields.Str(required=True) # Obligatorio
    model = fields.Str(required=True) # Obligatorio
    year = fields.Int(required=True)  # Obligatorio
