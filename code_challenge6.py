n = int(input("number of x: "))
z = 1

for x in range(n):
    for y in range(x + 1):
        print(z, end="\t")
        z += 1
    print("\n")

