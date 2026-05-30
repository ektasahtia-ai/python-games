health = 100

print("Zombie Survival Game")

while health > 0:
    action = input("Run or Fight? ")

    if action.lower() == "fight":
        health -= 20
        print("You fought a zombie!")
    elif action.lower() == "run":
        print("You escaped!")
    else:
        print("Invalid action!")

    print("Health:", health)

print("You died!")