# Menu Driven Program, Make a Student report and store data in file

while True:
    print("1. Add")
    print("2. Display")
    print("3. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        f = open("sudo.txt", "a")
        studentName = input("Enter name:")
        studentMarks = input("Enter marks:")
        f.write(studentName.center(20," ") + studentMarks.center(20, " ") + "\n")
        f.close()
    elif choice == "2":
        print("".center(40, "-"))
        print("Name".center(20," ") + "Marks".center(20, " "))
        print("".center(40, "-"))

        f = open("sudo.txt", "r")
        for line in f:
            print(line, end="")
            print("".center(40, "-"))
        
        f.close() 
    else:
        break