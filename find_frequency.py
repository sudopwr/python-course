# Program to find frequency of given number
no = int(input("Enter total no. of element:"))
sum = 0

noList = []

print("--------------------------")
for i in range(0, no):
    noList.append(int(input("Enter number:")))

targetElement = 0
checkedNoList = []
for i in range(0, no):
    targetElement = noList[i]
    targetElementFrequency = 0

    if targetElement in checkedNoList:
        continue

    checkedNoList.append(targetElement)

    for i in range(0, no):
        if noList[i] == targetElement:
            targetElementFrequency+=1

    print("{} : {}".format(targetElement, targetElementFrequency))        
