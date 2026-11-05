water = int(input("How much water do you have? "))
sun = input("is it high noon? ")
if sun == "yes":
    sun = True
else:
    sun = False
        

while sun == True and water != 0:
    water -= 1
    if water != 0:
        print("Water Level is", water)
    elif water == 0:
        print("Drum is Empty!")