# Input from the user
userInput = int(input("Pick a number: "))
# Check Values
if userInput % 3 == 0:
    print("Pling")
elif userInput % 5 == 0:
    print("Plang")
elif userInput % 7 == 0:
    print("Plong")
else:
    print(userInput)