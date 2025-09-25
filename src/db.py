#db.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

#load environmeent variables
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase=create_client(url,key)

#create Veihcles table
def create_Vehicles(vehicle_number,vehicle_type ,manufacturer,year_of_manufacture ,date_of_registration):
    return supabase.table("Vehicles").insert({
        "vehicle_number":vehicle_number,
        "vehicle_type":vehicle_type,
        "manufacturer":manufacturer,
        "year_of_manufacture":year_of_manufacture,
        "date_of_registration":date_of_registration,
        "Completed":False
    }).execute()

#get all tasks
def get_all_Vehicles():
    return supabase.table("Vehicles").select("*").order("date_of_registration").execute()

#update tasks status
def update_Vehicles(vehicle_id,completed=True):
    return supabase.table("Vehicles").update({"Completed":completed}).eq("vehicle_id",vehicle_id).execute()

#delete task
def delete_Vehicles(vehicle_id):
    return supabase.table("Vehicles").delete().eq("vehicle_id",vehicle_id).execute()

