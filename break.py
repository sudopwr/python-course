# calculate total of numbers as per user want
sum = 0
while True:
    number = int(input("Enter number : "))
    sum = sum + number

    doYouWantContinue = input("do you want to continue(y/n): ")
    if doYouWantContinue == 'n':
        break;

print("Total is", sum)
