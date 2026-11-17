route = ["Terminal", "Perez Park", "Pacific Mall"]

passengers = []
Seats = 6
Fare = 13
total = 0

print("----------------------\n\tMENU\n----------------------\n"
    "1 = Sakay\n"
    "2 = Priority Seat\n"
    "3 = Para po!\n"
    "4 = Baba sa Pinto\n"
    "5 = Baba sa Harap\n"
    "6 = Seat Check\n"
    "7 = Balikan\n"
    "8 = Exit\n----------------------")
while True:
    print()
    print("----------------------\nSakay:", passengers)
    print(len(passengers), "of", Seats, "seats\n----------------------")
    choice = input("Choice ----> ")
    
    
    if choice == "1":
        if len(passengers) == Seats:
            print("PUNO NA!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total += Fare
            print(name, "boarded at the back.")
            
    elif choice == "2":
        if len(passengers) == Seats:
            print("PUNO NA!")
        else:
            name = input("Name: ")
            passengers.insert(0, name)
            total += Fare
            print(name, "took the priority seat")
            
    elif choice == "3":
        name = input("Who's getting off? ")
        if name in passengers:
            passengers.remove(name)
            print(name, "got off. Ingat!")
        else:
            print(name, "is not in this jeep.")
            
    elif choice == "4":
        if len(passengers) == 0:
            print("The jeep is Empty.")
        else: 
            left = passengers.pop()
            print(left, "got off the door")
            
    elif choice == "5":
        if len(passengers) == 0:
            print("The jeep is Empty.")
        else:
            front = passengers.pop(0)
            print(front, "got off at the front")
    elif choice == "6":
        for i in range(len(passengers)):
            print("Seat", i+1, "=", passengers[i])
            
    elif choice == "7":
        route.reverse()
        print("Route:", route)
        
    elif choice == "8":
        print("Total Fare Today:", total)
        break
    
    else:
        print("invalid Input.")
        
        
        