from pydantic import BaseModel

class VehicleCreate(BaseModel):
    name: str
    model: str
class TelemetryCreate(BaseModel):
    vehicle_id: int
    speed: int
    fuel_level: int
    engine_temp: int