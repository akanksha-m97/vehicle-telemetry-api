from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from models import create_vehicle_table,create_telemetry_table
from database import get_db_connection
from schemas import VehicleCreate
from schemas import TelemetryCreate

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

create_vehicle_table()
create_telemetry_table()

@app.get("/")
def root():
    return {"message": "Vehicle Telemetry API running"}

@app.post("/vehicles")
def create_vehicle(vehicle: VehicleCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO vehicles (name, model) VALUES (?, ?)",
        (vehicle.name, vehicle.model)
    )

    conn.commit()
    conn.close()

    return {"message": "Vehicle added successfully"}
@app.get("/vehicles")
def get_vehicles():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM vehicles")
    vehicles = cursor.fetchall()

    conn.close()

    return {"vehicles": [dict(v) for v in vehicles]}

@app.post("/telemetry")
def add_telemetry(data: TelemetryCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO telemetry (vehicle_id, speed, fuel_level, engine_temp)
        VALUES (?, ?, ?, ?)
        """,
        (data.vehicle_id, data.speed, data.fuel_level, data.engine_temp)
    )

    conn.commit()
    conn.close()

    return {"message": "Telemetry data added"}

@app.get("/telemetry/{vehicle_id}")
def get_telemetry(vehicle_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT speed, fuel_level, engine_temp FROM telemetry WHERE vehicle_id = ?",
        (vehicle_id,)
    )

    telemetry_data = cursor.fetchall()
    conn.close()

    return {
        "vehicle_id": vehicle_id,
        "telemetry": [dict(row) for row in telemetry_data]
    }


@app.get("/ui", response_class=HTMLResponse)
def serve_ui():
    with open("frontend/index.html", "r") as f:
        return f.read()