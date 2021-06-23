# check are you allow to drive car?

isAge18 = input("is your age 18+ (y / n) : ")
doYouHaveLicense = input("do you have license (y / n): ")
doYouHaveAadharCard = input("do you have aadhar card (y / n): ")

if isAge18 == 'y':
    if doYouHaveLicense == 'y':
        if doYouHaveAadharCard == 'y':
            print("Allow")
        else:
            print("Not Allow")
    else:
        print("Not Allow")
else:
    print("Not Allow")