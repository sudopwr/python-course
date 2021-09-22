# Product reports - File storage using json lib
# Menu Driven Programs
import json

while True:
    print("1. Display")
    print("2. Add")
    print("3. Total")
    print("4. Remove")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        fileRead = open("product.txt", "r")
        products = json.load(fileRead)
        print("".center(50, "-"))
        print("No".center(10, " "), "Name".center(20, " "), "Price".center(20, " "))
        print("".center(50, "-"))
        index = 1
        for prod in products:
            print(str(index).center(10, " ") ,prod["name"].center(20, " "), str(prod["price"]).center(20, " "))
            print("".center(50, "-"))
            index = index + 1

        fileRead.close()
    elif choice == "2":
        fileRead = open("product.txt", "r")
        products = json.load(fileRead)
        fileRead.close()

        fileWrite = open("product.txt", "w")
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        prod = {
            "name": name,
            "price": price
        }
        products.append(prod)
        json.dump(products, fileWrite)
        fileWrite.close()
    elif choice == "3":
        fileRead = open("product.txt", "r")
        products = json.load(fileRead)
        fileRead.close()
        total = 0
        for prod in products:
            total = total + prod["price"]
        
        print("=========> Total is", total)
    elif choice == "4":
        removeIndex = int(input("Enter product no: "))

        fileRead = open("product.txt", "r")
        products = json.load(fileRead)
        fileRead.close()
        products.pop(removeIndex - 1)

        fileWrite = open("product.txt", "w")
        json.dump(products, fileWrite)
        fileWrite.close()
    else:
        print("Thank you!!")
        break