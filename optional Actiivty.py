for y in range(9):
    for x in range(5):
        if x + y >= 4 or x == 1 and y > 6:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()