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
    return ''.join(drops)