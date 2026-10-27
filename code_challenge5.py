n = int(input("number of x: "))
for x in range(n):
    for y in range(n):
        if x == y or y + x == n-1:
            print("*", end=" ")
        else:
            print("", end=" ")
    print()
