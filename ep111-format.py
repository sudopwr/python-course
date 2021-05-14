name = input("Enter Name: ")
no = input("Enter No: ")
salary = input("Enter Salary: ")

report = """-------- Employee Details -------
Employee No : {name} 
Employee name: {no} 
Employee Salary: {salary}"""

print(report.format(name=name, no=no, salary=salary))
