marks = int(input("Enter marks: "))

if marks >= 80:
    print("Grade A")
else:
    if marks >= 70:
        print("Grade B")
    else:
        if marks >= 60:
            print("Grade C")
        else:
            if marks >= 36:
                print("Grade D")
            else:
                print("Fail")
