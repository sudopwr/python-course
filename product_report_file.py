# Product reports - File storage 
# Menu Driven Programs

while True:
    print("1. Add")
    print("2. Display")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        file = open("product.txt", "a")
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        file.write(name.center(25, " ") + price.center(25, " ") + "\n")
        file.close()
    elif choice == "2":
        print("".center(50, "-"))
        print("Name".center(25, " "), "Price".center(25, " "))
        print("".center(50, "-"))

        file = open("product.txt", "r")
        for line in file:
            print(line, end="")
            print("".center(50, "-"))
    else:
        print("Thank you!")
        break