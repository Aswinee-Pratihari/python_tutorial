name=input("Enter your name")

match name:
    case "Virat" | "Rohit" | "Gautam":
        print("You are cricketer")
    case "Chetri":
        print("You are footballer")
    case "Sania":
        print("You are badminton player")
    case _:
        print("Who?")

