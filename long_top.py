student1Marks = int(input("Enter 1st student marks: "))
student2Marks = int(input("Enter 2nd student marks: "))
student3Marks = int(input("Enter 3rd student marks: "))
student4Marks = int(input("Enter 4th student marks: "))
student5Marks = int(input("Enter 5th student marks: "))

if student1Marks > student2Marks and student1Marks > student3Marks and student1Marks > student4Marks and student1Marks > student5Marks:
    print("1st student is topper with", student1Marks, "%")
elif student2Marks > student3Marks and student2Marks > student4Marks and student2Marks > student5Marks:
    print("2nd student is topper with", student2Marks, "%")
elif student3Marks > student4Marks and student3Marks > student5Marks:
    print("3rd student is topper with", student3Marks, "%")
elif student4Marks > student5Marks:
    print("4th student is topper with", student4Marks, "%")
else:
    print("5th student is topper with", student5Marks, "%")


