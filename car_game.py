command = ""
started = False
while True:
    command = (input("Enter your command or quit(q): ")).lower()
    if command == "quit" or "q":
        break

    if command == "start":
        if started:
            print("You have already started the car")
        else:
            started = True
            print("Car started")

    elif command == "stop":
        if not started:
            print("Car has already been stopped")
        else:
            started = False
            print("Car stopped")

    elif command == "help":
        print("""Commands:
        start - starts the game
        stop - stops the game
        quit - quits the game""")

    else:
        print("Invalid command")