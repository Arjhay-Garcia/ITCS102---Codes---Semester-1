n = int(input("Number: "))
m = n-1

for x in range(n):
    for y in range(n):
        if (x == 0 or y == 0 or x == m or y == m or x + y == m or x == y):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()