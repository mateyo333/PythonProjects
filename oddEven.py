import time  # Import the 'time' module to add pauses

def display_intro():
    """Prints the introduction to the game."""
    print("Welcome, brave adventurer!")
    time.sleep(1)  # Pause for 1 second
    print("You find yourself standing at a mysterious Crossroads.")
    time.sleep(1)
    print("To the north, you see a shadowy Forest.")
    print("To the east, there's a dark Cave entrance.")
    print("To the west, you hear the rushing sound of a River.")
    print("To the south, the path seems to lead back from where you came.")
    print("What will you do?")
    print()

def get_player_choice():
    """Gets the player's choice of direction."""
    while True:
        choice = input("Enter your direction (north, east, west, south) or 'quit': ").lower()
        if choice in ["north", "east", "west", "south", "quit"]:
            return choice
        else:
            print("Invalid direction. Please try again.")

def handle_forest():
    """Handles the outcome of choosing the Forest."""
    print("\nYou venture into the shadowy Forest...")
    time.sleep(1.5)
    print("The trees are dense, and the air is still.")
    time.sleep(1.5)
    # Let's add a simple random element
    import random
    if random.randint(1, 2) == 1:
        print("You stumble upon a hidden treasure chest! You found 10 gold coins!")
    else:
        print("You hear a rustling in the bushes... it's just a squirrel.")
    print("You decide to head back to the Crossroads.")
    time.sleep(1)
    return "crossroads" # The player returns to the crossroads

def handle_cave():
    """Handles the outcome of choosing the Cave."""
    print("\nYou cautiously enter the dark Cave...")
    time.sleep(1.5)
    print("It's damp and cold. You can hear water dripping.")
    time.sleep(1.5)
    print("Suddenly, you hear a growl!")
    time.sleep(1)
    print("A small bat flies past your head. You sigh in relief.")
    print("You decide the cave is too spooky and return to the Crossroads.")
    time.sleep(1)
    return "crossroads"

def handle_river():
    """Handles the outcome of choosing the River."""
    print("\nYou walk towards the rushing River...")
    time.sleep(1.5)
    print("The water looks cold and the current is strong.")
    time.sleep(1.5)
    print("You see a rickety old bridge.")
    choice = input("Do you try to cross the bridge? (yes/no): ").lower()
    if choice == "yes":
        print("You carefully make your way across the bridge.")
        time.sleep(1)
        print("You reach the other side safely.")
        return "other_side" # A new location!
    else:
        print("You decide it's too risky and head back to the Crossroads.")
        time.sleep(1)
        return "crossroads"

def handle_other_side():
    """Handles the outcome of being on the other side of the river."""
    print("\nYou are on the other side of the river.")
    time.sleep(1)
    print("The path ahead looks promising.")
    print("For now, there's nothing else to do here. You decide to go back.")
    time.sleep(1)
    return "crossroads"

# --- Main Game Loop ---
current_location = "crossroads"
player_name = input("Enter your name, brave adventurer: ")
print(f"Welcome, {player_name}!")
time.sleep(1)

while True:
    if current_location == "crossroads":
        display_intro()
        choice = get_player_choice()
        if choice == "north":
            current_location = handle_forest()
        elif choice == "east":
            current_location = handle_cave()
        elif choice == "west":
            current_location = handle_river()
        elif choice == "south":
            print("\nYou decide to head back the way you came. The adventure ends here.")
            break
        elif choice == "quit":
            print("\nThanks for playing!")
            break
    elif current_location == "other_side":
        current_location = handle_other_side()
    else:
        print("Error: Unknown location!")
        break

print("\nGame Over.")