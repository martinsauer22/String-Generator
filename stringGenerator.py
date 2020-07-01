#!/usr/bin/env python3

import random 
import string

# function that returns random string
def generateString(stringSize): 
	stringFinal = ""
	for i in range(stringSize): 
		stringFinal += random.choice(string.ascii_lowercase)
	return stringFinal

# ask for size 
stringSize = int(input("Enter size of string: ")) 

# check if size is valid 
if stringSize <= 0: 
	exit("Error: You entered an invalid number!") 

# print out string 
print(generateString(stringSize)) 
