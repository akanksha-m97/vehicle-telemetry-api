## 🚗 Vehicle Telemetry Backend API

A backend application built using FastAPI to manage vehicles and store telemetry
data such as speed, fuel level, and engine temperature.

## 🚀 Features
- Add vehicles
- Add telemetry data for vehicles
- View telemetry data
- Input validation
- SQLite database
- Simple frontend using HTML & JavaScript

## 🛠️ Tech Stack
- Python
- FastAPI
- SQLite
- HTML, JavaScript
- Uvicorn

## 📂 Project Structure

vehicle-telemetry-api/<br>
├── frontend/<br>
│   ├── index.html<br>
│   └── script.js<br>
├── main.py<br>
├── models.py<br>
├── schemas.py<br>
├── database.py<br>
├── telemetry.db<br>
├── .gitignore<br>
└── README.md<br>

## ▶️ How to Run

1. Create virtual environment
python -m venv .venv

2. Activate virtual environment
.venv\Scripts\activate

3. Install dependencies
pip install fastapi uvicorn

4. Run server
uvicorn main:app --reload

## 🔗 Application URLs

- **Backend Server**  
  http://127.0.0.1:8000

- **Frontend UI**  
  http://127.0.0.1:8000/ui

- **API Documentation (Swagger UI)**  
  http://127.0.0.1:8000/docs

---


## 📦 Example Telemetry Payload

{<br>
  "vehicle_id": 1,<br>
  "telemetry": [<br>
    {<br>
      "speed": 80,<br>
      "fuel_level": 60,<br>
      "engine_temp": 90<br>
    }
  ]
}

## 👩‍💻 Author

**Akanksha**  
B.Tech CSE, IGDTUW  
