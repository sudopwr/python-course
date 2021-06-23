# check identity for vaccine registration ???

doYouHaveAadharCard = input("Do you have aadhar card (y / n) : ")
doYouHaveVotingCard = input("Do you have voting card (y / n) : ")
doYouHavePassport = input("Do you have passport (y / n) : ")

if doYouHaveAadharCard == 'y' or doYouHaveVotingCard == 'y' or doYouHavePassport == 'y':
    print("Allow")
else:
    print("Not Allow")