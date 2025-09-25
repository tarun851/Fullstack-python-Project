# vehicle management system

This project manages vehicle information in an organization. It stores key details like vehicle number, type, manufacturer, year,date of registration in a database. The system helps track vehicles efficiently, ensures proper assignment, and supports easy retrieval of vehicle records.

# features
-**Vehicle Registration & Details**:
Add new vehicles with details like Vehicle ID, Type (Car, Truck, Bike), Brand, Model, Year, Color, and Registration Number.
-**Owner / Driver Management**:
Store information about vehicle owners or drivers: Name, Contact, License Number, Address.
-**Vehicle Tracking & Status**:
Track current status: Available, In Use, Under Maintenance, Reserved.
-**Maintenance & Service Records**:
Log service history, repairs, and scheduled maintenance.
Track cost, service date, and next due date.
-**Fuel Management**:
Record fuel usage, cost, and mileage for each vehicle.
-**Trip / Usage Management**:
Log trips, start & end time, distance traveled, driver assigned.
Calculate trip cost, fuel consumption, or utilization.
-**Alerts & Notifications**:
Send reminders for maintenance, registration renewal, insurance expiry, or pending trips.
-**Reports & Analytics**:
Generate reports: Vehicle usage, maintenance cost, fuel efficiency, driver performance.

## project structure

Vehicle_management_system/ 
|
|-------src/                 #core application logic and database 
|        |--logic.py         #business logic and tasks
|        |--db.py            #Database operations
|
|-------api/                 #backend API
|        |--main.py          #fastAPI endpoints
|
|-------frontend/            #Frontend application
|        |--app.py           #streamlit web interface
|
|-------requirements.txt     #python dependencies
|
|-------READ.md              #Project documentation
|
|-------.env                 #Python Variables



## Quick start

## Prerequisites

-Python 3.8 or higher
-A supabase account
-Git(Push)


## Cloning or downloading the project 
# option 1: Clone with Git
git clone <repository-url>

## option 2:Download and extract the ZIP file

## 2. install dependencies

## install all required python packages

pip install -r requirements.txt

## 3.set up supabase Database

1.Create a supabase Project :

2.Create the task table

-Go to sql editor in your Supabase daseboard

-Run This SQL command:

```sql
    CREATE TABLE Vehicles (
    vehicle_id INT PRIMARY KEY,
    vehicle_number VARCHAR(15) NOT NULL,
    vehicle_type VARCHAR(20) NOT NULL,
    manufacturer VARCHAR(50),
    year_of_manufacture INT,
    date_of_registration DATE
);


```
3.Get your credentials

## 4, Configure environmental variables

 1. Create a `.env` file in the project root

 2. Add your supabase credentials to `.env`:
    SUPABASE_URL=your_project_url_here
    SUPABASE_KEY=your_anon_key_here

-**example:**
 SUPABASE_URL=https://jiowiicmcehcexntulvc.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imppb3dpaWNtY2VoY2V4bnR1bHZjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODE4ODksImV4cCI6MjA3MzY1Nzg4OX0.zoBvzXygTnPvjDSoOmsBvpNhYNCvF4wsqoxcQIzd9TM

## 5.Run the application

## streamlit Frontend
streamlit run frontend/app.py

the app will open in your browser at `http://localhost:8000`

## how to use

## Technical Details

## Technologies used

-**Frontend**:Streamlit (Python web framework)
-**Backend**:FastAPI(Python REST API Framework)
-**Database**:supabase(PostgresSQL-based-Backend-as-a-service)
-**languages**:python 3.8+

## Key components:

1. **`src/db.py`** :Database operations
-handles all CRUD operations on Supabase

2. **`src/logic.py`**:Business logic
-Task validation and porcessing

## Troubleshooting

##  common issues

## Future Enhancements 

## support
 
If you enconter any issues or have any questions:
phone:+91 8328362958
Email:tarunkumar271205@gmail.com




