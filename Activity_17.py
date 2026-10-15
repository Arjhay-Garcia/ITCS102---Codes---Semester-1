num = int(input("Enter a Number: "))
nom = num

for w in range(0, num+1):
    for i in range(11):
        print(nom, "x", i, "=", int(nom * i), end="\t")
    print("\n")
    nom -= 1
