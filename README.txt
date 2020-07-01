This is a simple String generator 

The user can input a number (size) and the program will output a random String containing just letters 

Idea: 
	- user inputs a positive number 
		=> size of string to output 
	- number gets handed over to function generateString()  
		- creates empty string 
		- chooses a random letter from string.ascii_lowercase and adds it to string 
		- gets repeated until final size is reached 
		- return string 
