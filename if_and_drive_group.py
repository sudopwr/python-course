# check are you allow to drive car?

isAge18 = input("is your age 18+ (y / n) : ")
doYouHaveLicense = input("do you have license (y / n): ")
doYouHaveAadharCard = input("do you have aadhar card (y / n): ")
doYouHaveVotingCard = input("do you have Voting card (y / n): ")

if isAge18 == 'y' and doYouHaveLicense == 'y' and (doYouHaveAadharCard == 'y' or doYouHaveVotingCard == 'y'):
    print("Allow")
else:
    print("Not Allow")