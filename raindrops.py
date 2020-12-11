def check_input(value):
    # Input in a while loop to check for valid inputs
    while True:
        try:
    # Input from the user
            userInput = int(input(value))   
        except ValueError:
            print("Sorry, please use an integer")
            continue
        else:
            break
    return userInput

# Check Values Function
def raindrop():
    if userInput % 3 == 0:
        print("Pling")
    elif userInput % 5 == 0:
        print("Plang")
    elif userInput % 7 == 0:
        print("Plong")
    else:
        print(userInput)

userInput = check_input("Pick a number: ")
raindrop()