from marshmallow import Schema, fields, validate, ValidationError, validates_schema # type: ignore

class VehicleDTO(Schema):
    id = fields.Int(dump_only=True)
    car_brand = fields.Str(
        required=True, 
        validate=[validate.Length(min=2, max=100)]
    )
    arrival_location = fields.Str(
        required=True,
        validate=[validate.Length(min=2, max=100)]
    )
    applicant = fields.Str(
        required=True,
        validate=[
            validate.Length(min=2, max=100),
            validate.Regexp(r"^[A-Za-z\s]+$", error="El nombre del aspirante solo puede contener letras y espacios")
        ]
    )

    @validates_schema
    def validate_fields(self, data, **kwargs):
        if any(char.isdigit() for char in data.get("car_brand", "")):
            raise ValidationError("La marca del carro no puede contener números", field_name="car_brand")
        if any(char.isdigit() for char in data.get("arrival_location", "")):
            raise ValidationError("La localidad de llegada no puede contener números", field_name="arrival_location")
