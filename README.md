# Cycling Tracker

A simple Python program to track your bike rides. This program allows you to record details about your cycling activities and view your ride history.

## Features

* **Add New Ride:** Record the distance, duration, date, and optional notes for each bike ride.
* **View Rides:** Display a list of all recorded rides, including date, distance, duration, and calculated average speed. Any notes you added for the ride are also shown.
* **Data Persistence:** Your ride history is saved to a `cycling_history.json` file in the same directory as the script, so your data is preserved between program runs.

## Getting Started

1.  **Save the Code:** Save the Python code (provided in the previous response) as `cycling_tracker.py` in a directory of your choice.

2.  **Run the Program:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run the program using the command:
    ```bash
    python cycling_tracker.py
    ```

## How to Use

Once the program starts, you will see a menu with the following options:

1.  **Add New Ride:**
    * Select `1` and press Enter.
    * The program will prompt you to enter the following details for your ride:
        * Distance (in kilometers)
        * Duration (in minutes)
        * Date (in YYYY-MM-DD format)
        * Any notes about the ride (optional)
    * After entering the information, the ride will be added to your history and saved.

2.  **View Rides:**
    * Select `2` and press Enter.
    * The program will display a list of all the rides you have recorded, showing the date, distance, duration, average speed (if applicable), and any notes.

3.  **Exit:**
    * Select `3` and press Enter to close the Cycling Tracker program. Your latest ride data will be saved before the program exits.

## Data Storage

The program stores your ride history in a JSON file named `cycling_history.json`. This file will be created in the same directory where you run the `cycling_tracker.py` script. You do not need to interact with this file directly.



Improvements I can make

* **Calculating Total Statistics:** Add a menu option to display the total distance ridden, total time spent cycling, and the overall average speed.
* **Filtering Rides:** Implement a feature to filter rides by date range or keywords in the notes.
* **Input Validation:** Enhance the input validation to ensure users enter data in the correct format (e.g., date format checking).
* **Error Handling:** Add more robust error handling for file operations.
* **Basic Data Analysis:** Explore simple data analysis like finding the longest ride or the fastest average speed.
* **Graphical User Interface (GUI):** For a more user-friendly experience, consider using a GUI library like Tkinter to create a visual interface.

