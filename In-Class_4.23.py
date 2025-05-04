username = input("What is your username?")


if username.lower() == "usmanrizvi":
    password = input("What is your password?")
    if password.lower() == "password123":
        print("You may login, Welcome!")
    else:
        print("Invalid password")
else:
    print("Invalid username")_