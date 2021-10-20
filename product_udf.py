# UDF - User define function
import json

def read_file():
    fileRead = open("product.txt", "r")
    products = json.load(fileRead)
    fileRead.close()
    return products

def write_file(products):
    fileWrite = open("product.txt", "w")
    json.dump(products, fileWrite)
    fileWrite.close()

while True:
    print("1. Display")
    print("2. Add")
    print("3. Total")
    print("4. Remove")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        products = read_file()
        print("".center(50, "-"))
        print("No".center(10, " "), "Name".center(20, " "), "Price".center(20, " "))
        print("".center(50, "-"))
        index = 1
        for prod in products:
            print(str(index).center(10, " ") ,prod["name"].center(20, " "), str(prod["price"]).center(20, " "))
            print("".center(50, "-"))
            index = index + 1

    elif choice == "2":
        products = read_file()

        fileWrite = open("product.txt", "w")
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        prod = {
            "name": name,
            "price": price
        }
        products.append(prod)
        write_file(products)
    elif choice == "3":
        products = read_file()
        total = 0
        for prod in products:
            total = total + prod["price"]
        
        print("=========> Total is", total)
    elif choice == "4":
        removeIndex = int(input("Enter product no: "))

        products = read_file()
        products.pop(removeIndex - 1)

        write_file(products)
    else:
        print("Thank you!!")
        break