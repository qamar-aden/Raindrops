#Input in a while loop to check for valid inputs
while True:
    try:
# Input from the user
        userInput = int(input("Pick a number: "))   
    except ValueError:
        print("Sorry, please use an integer")
        continue
    else:
        break

# Check Values
if userInput % 3 == 0:
    print("Pling")
elif userInput % 5 == 0:
    print("Plang")
elif userInput % 7 == 0:
    print("Plong")
else:
    print(userInput)