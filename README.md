# Raindrops
The function in this script takes a number as it's input (x) and converts it to a string, the contents of
which depend on the numbers factors:

* if the number has a factor of 3, output 'Pling'
* if the number has a factor of 5, output 'Plang'
* if the number has a factor of 7, output 'Plong'
* if the number does not have any of the above as a factor simply return the numbers digits

Examples
* 28's factors are 1, 2, 4, 7, 14 and 28: this would be a simple 'Plong'
* 30's factors are 1, 2, 3, 5, 6, 10, 15, 30: this would be a 'PlingPlang'
* 34 has four factors: 1, 2, 17, and 34: this would be '34'

To run the script with manual inputs:
```
python3 raindrops-manual-input.py
```
To test the script:
```
python raindrops-test.py
```