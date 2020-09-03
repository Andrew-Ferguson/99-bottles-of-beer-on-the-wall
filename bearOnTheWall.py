wallOfBeer = True

print("")
print("")
print("------------------------------")
print("99 bottles of beer on the wall")
print("")

yesOrNo = input("beer or custom - b/c : ").lower()

if yesOrNo == "b":
    amount = 99
    while wallOfBeer == True:
        print("")
        print(amount, "bottles of beer on the wall")
        print(amount, "bottles of a beer")
        print("take one down pass it around")
        amount = amount - 1
        if amount == 0:
            wallOfBeer = False
            print("No more bottles of beer on the wall")
        if wallOfBeer == True:
            print(amount, "bottles of beer on the wall")
        print("")

if yesOrNo == "c":
    thingsOnWall = input("Enter a thing to put on the wall: ")
    amount = int(input("Enter the number of things you want on the wall: "))
    while wallOfBeer == True:
        print("")
        print(amount, "bottles of", thingsOnWall, "on the wall")
        print(amount, "bottles of a", thingsOnWall)
        print("take one down pass it around")
        amount = amount - 1
        if amount == 0:
            wallOfBeer = False
            print("No more bottles of", thingsOnWall, "on the wall")
        if wallOfBeer == True:
            print(amount, "bottles of", thingsOnWall, "on the wall")
        print("")
