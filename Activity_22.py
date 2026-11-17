rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
fav = []

while True:
    ask = input("do you know the colors of the rainbow? (yes/no)")
    if ask.lower() == "yes":
        for x in rainbow:
            print(x, ",", end="")
        favask = str(input("\nWhat's your favorite color in the Rainbow?"))
        if favask in rainbow:
            fav.append(favask)
            print("Your Favorite color in colors of rainbow is/are ", fav)
            break
        else:
            print("Color not in Rainbow")
            continue
    else:
        break
    