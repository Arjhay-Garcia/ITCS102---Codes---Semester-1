password = "Hello World!"

while True:
    user = input("What's your name? ")
    word = str(input("What's the Password? "))

    if word == password:
        print("\nAccess granted!\n\nWelcome!", user)
        break
    else:
        print("Wrong Password!!")
        continue