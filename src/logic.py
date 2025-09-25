# src/logic.py

from src import db

class VehiclesManager:
    """
    Acts as a bridge b/w frontend (Streamlit/FastAPI) and the database
    """

    def __init__(self):
        # Create a database manager instance (this will handle actual DB operations)
        self.db = db

    # ----- Create -----
    def add_Vehicles(self, vehicle_number, vehicle_type, manufacturer=None, year_of_manufacture=None, date_of_registration=None):
        """
        Add a new Vehicles record to the database.
        Returns the success message if the Vehicles record is added.
        """
        if not vehicle_number or not vehicle_type:
            return {"success": False, "message": "vehicle_number & vehicle_type are required"}

        # Call DB method to insert Vehicles
        result = self.db.create_Vehicles(vehicle_number, vehicle_type, manufacturer, year_of_manufacture, date_of_registration)

        if result.get("success"):
            return {"success": True, "message": "Vehicles record added successfully"}
        else:
            return {"success": False, "message": f"Error: {result.get('error')}"}

    # ----- Read -----
    def get_Vehicles(self):
        """
        Get all Vehicles records from the database
        """
        return self.db.get_all_Vehicles()

    # ----- Update -----
    def mark_Vehicles_completed(self, vehicle_id):
        """
        Mark a Vehicles record as completed (or serviced)
        """
        result = self.db.update_Vehicles(vehicle_id, True)
        if result.get("success"):
            return {"success": True, "message": "Vehicles record marked as completed"}
        return {"success": False, "message": f"Error: {result.get('error')}"}
    
    # ----- Mark vehicle as pending -----
    def mark_Vehicles_pending(self, vehicle_id): 
        """ Mark a Vehicles record as pending (or serviced) """ 
        result = self.db.update_Vehicles(vehicle_id, False)
        if result.get("success"): 
            return {"success": True, "message": "Vehicles record marked as pending"} 
        return {"success": False, "message": f"Error: {result.get('error')}"}

    # ----- Delete -----
    def delete_Vehicles(self, vehicle_id):
        """
        Delete a Vehicles record from the database
        """
        result = self.db.delete_Vehicles(vehicle_id)
        if result.get("success"):
            return {"success": True, "message": "Vehicles record deleted successfully"}
        return {"success": False, "message": f"Error: {result.get('error')}"}
