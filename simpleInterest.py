car_started = False

while True:
    command = input("Enter a command ('start' for ignition, 'stop' to turn off, 'help' for options, 'quit' to exit): ").lower()

    if command == "help":
        print("start - to turn the ignition on")
        print("stop - to turn the ignition off")
        print("quit - to exit")
    elif command == "start":
        if car_started:
            print("Car is already running.")
        else:
            print("Starting the engine... Vroom vroom!")
            car_started = True
    elif command == "stop":
        if car_started:
            print("Turning off the engine...")
            car_started = False
        else:
            print("Car is already off.")
    elif command == "quit":
        print("Exiting.")
        break
    else:
        print("Invalid command. Type 'help' for available options.")

print("Goodbye.")