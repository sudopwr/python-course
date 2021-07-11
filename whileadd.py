# print total sum of numbers from 1 to given user number
number = int(input("Enter number: "))

sum = 0
bar = 1
while bar <= number:
    if bar % 2 == 0:
        sum = sum + bar

    bar = bar + 1

print("Total is", sum)

