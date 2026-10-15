num = int(input("Enter a Number: "))

for i in range(10, 0, -1):
    print(num, "x", i, "=", int(num * i), end="\t")
    
