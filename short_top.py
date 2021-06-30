student1Marks = int(input("Enter 1st student marks: "))
student2Marks = int(input("Enter 2nd student marks: "))
student3Marks = int(input("Enter 3rd student marks: "))
student4Marks = int(input("Enter 4th student marks: "))
student5Marks = int(input("Enter 5th student marks: "))

topperStudentMarks = student1Marks
topperStudentName = '1st'

if student2Marks > topperStudentMarks:
    topperStudentMarks = student2Marks
    topperStudentName = '2nd'

if student3Marks > topperStudentMarks:
    topperStudentMarks = student3Marks
    topperStudentName = '3rd'

if student4Marks > topperStudentMarks:
    topperStudentMarks = student4Marks
    topperStudentName = '4th'

if student5Marks > topperStudentMarks:
    topperStudentMarks = student5Marks
    topperStudentName = '5th'


print(topperStudentName, " student is topper with", topperStudentMarks, "%")

