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

# Raindrops Function
def get_raindrops(x):
    # Put drops in array
    drops = []
    # Append array with values from 3,5,7 factors
    if (x % 3 == 0):
        drops.append("Pling")
    if (x % 5 == 0):
        drops.append("Plang")
    if (x % 7 == 0):
        drops.append("Plong")
    if not drops:
        return str(x)
    print(''.join(drops))
    return ''.join(drops)

userInput = check_input("Pick a number: ")
get_raindrops(userInput)