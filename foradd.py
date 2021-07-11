# print total sum of numbers from 1 to given user number
number = int(input("Enter number: "))

sum = 0
for bar in range(1, number+1):
    if bar % 2 == 0:
        sum = sum + bar

print("Total is", sum)
