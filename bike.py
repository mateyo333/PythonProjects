# Initialize an empty list to store ride data
rides = []

def add_ride():
    """Allows the user to enter information about a bike ride."""
    print("\n--- Add New Ride ---")
    try:
        distance = float(input("Enter the distance of your ride (in km): "))
        duration_minutes = int(input("Enter the duration of your ride (in minutes): "))
        date = input("Enter the date of your ride (YYYY-MM-DD): ")
        notes = input("Any notes about this ride? ")

        ride_data = {
            "distance": distance,
            "duration": duration_minutes,
            "date": date,
            "notes": notes
        }
        rides.append(ride_data)
        print("\nRide added successfully!")
    except ValueError:
        print("\nInvalid input. Please enter numbers for distance and duration.")

def view_rides():
    """Displays the recorded bike rides."""
    if not rides:
        print("\nNo rides recorded yet.")
        return

    print("\n--- Your Rides ---")
    for i, ride in enumerate(rides):
        print(f"\nRide #{i+1}:")
        print(f"  Date: {ride['date']}")
        print(f"  Distance: {ride['distance']} km")
        print(f"  Duration: {ride['duration']} minutes")
        if ride['duration'] > 0 and ride['distance'] > 0:
            speed_kmh = (ride['distance'] / (ride['duration'] / 60))
            print(f"  Average Speed: {speed_kmh:.2f} km/h")
        else:
            print("  Average Speed: N/A")
        if ride['notes']:
            print(f"  Notes: {ride['notes']}")

def main():
    """Main function to run the cycling program."""
    while True:
        print("\n--- Cycling Tracker ---")
        print("1. Add New Ride")
        print("2. View Rides")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_ride()
        elif choice == '2':
            view_rides()
        elif choice == '3':
            print("\nExiting the Cycling Tracker. Happy riding!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()