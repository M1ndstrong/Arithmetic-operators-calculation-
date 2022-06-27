"""Creating a code to output the calculation of two numbers
input by the user using all arithmetic operators """

# creating the user's input to calculate 
num_1 = input ("Input a number; ")
num_2 = input ("Input a second number; ")

'''define the results of the user's input in arithmetic operators,
casting the data type as float to make it readable, and for 
user to input a float number for calculation, floor division (//) included
'''

sum = ("The sum is : ", float (num_1) + float (num_2))
minus = ("The substraction is : ", float (num_1) - float (num_2))
mul_ = ("The multiplication is : ", float (num_1) * float (num_2))
divide = ("The division is : ", float (num_1) / float (num_2))
Modulus = ("The Modulus is : ", float (num_1) %  float (num_2))
Exponentiation = ("The Exponentiation is : ", float (num_1) ** float (num_2))
Floor_division = ("The Floor division is : ", float (num_1)  // float (num_2))

# Printing out the output;

def calculation (a, b):
    print (sum)
    print (minus)
    print (mul_)
    print (divide)
    print (Modulus)
    print (Exponentiation)
    print (Floor_division)
    
calculation (num_1, num_2)
