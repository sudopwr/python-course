# python 3 product report

products = []

while True:
    prod = {}
    prod["name"] = input("Enter product name: ")
    prod["price"] = input("Enter product price: ")
    products.append(prod)

    if input("Do you want to add new product(y/n):") == "n":
        break;

print("".center(50, "-"))
print("Name".center(25, " "), "Price".center(25, " "))
print("".center(50, "-"))

for prod in products:
    print(prod["name"].center(25, " "), prod["price"].center(25, " "))
    print("".center(50, "-"))
