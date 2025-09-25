# api/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Import VehiclesManager from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import VehiclesManager

# ------------------------------------ App setup ----------------------
app = FastAPI(title="Vehicle Manager API", version="1.0")

# --------------- Allow frontend (Streamlit/React) to call the API ---------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # fixed typo: was allow_origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]      # fixed typo: was allow_handlers
)

# Create a VehiclesManager instance (business logic)
vehicles_manager = VehiclesManager()

# --------- Data Models ---------
class VehicleCreate(BaseModel):
    """
    Schema for creating a vehicle
    """
    vehicle_number: str
    vehicle_type: str
    manufacturer: str
    year_of_manufacture: int
    date_of_registration: str

class VehicleUpdate(BaseModel):
    """
    Schema to update the vehicle status
    """
    completed: bool

# ------------ Endpoints ---------
@app.get("/")
def home():
    """Check if the API is running"""
    return {"message": "Vehicle Manager API is running!"}

@app.get("/Vehicles")
def get_Vehicles():
    """Get all vehicles"""
    return vehicles_manager.get_Vehicles()

@app.post("/Vehicles")
def create_Vehicles(vehicle: VehicleCreate):
    """Add a new vehicle"""
    result = vehicles_manager.add_Vehicles(
        vehicle.vehicle_number,
        vehicle.vehicle_type,
        vehicle.manufacturer,
        vehicle.year_of_manufacture,
        vehicle.date_of_registration
    )
    if not result.get("success"):          # fixed key: was "Success"
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.put("/Vehicles/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle: VehicleUpdate):
    """Mark vehicle as complete or pending"""
    result = (
        vehicles_manager.mark_Vehicles_completed(vehicle_id)
        if vehicle.completed else vehicles_manager.mark_Vehicles_pending(vehicle_id)
    )
    if not result.get("success"):          # fixed key: was "Success"
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.delete("/Vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    """Delete a vehicle"""
    result = vehicles_manager.delete_Vehicles(vehicle_id)
    if not result.get("success"):          # fixed key: was "Success"
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

# ------------- Run ----------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
