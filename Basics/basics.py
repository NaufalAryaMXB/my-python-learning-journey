#variables and data structure

# name = "John" #string

# age = 30 #integer

# has_license = True #boolean

# height = 5.9 #float

#print variables
# print("Name:", name)
# print("Age:", age)
# print("Has License: ", has_license)
# print("Height: ", height)

#user input
# print('user Input')
# nameinput = input("Name : ")
# Ageinput = input("Age : ")
# print("printing user input")
# print("Name : ", nameinput)
# print("Age : ", Ageinput)

#arithmetic operators
# print("arithmetic operators")
# num1 = 10
# num2 = 20
# print("num1 + num2 : ",int( num1 + num2)) #addition and force to  be integer
# print("num1 - num2 : ", num1 - num2) #subtraction
# print("num1 * num2 : ", num1 * num2) #multiplication
# print("num1 / num2 : ", num1 / num2) #division
# print("num1 % num2 : ", num1 % num2) #modulo
# print("num1 ** num2 : ", num1 ** num2) #exponentiation
# print("num1 // num2 : ", num1 // num2) #floor division

#string methods
string = '   hElLo pyThon 123   '
print("this is the original string :", string)
print("this is to see the type method : ",type(string)) #to see variable type
print("this is to see the lower method : ",string.lower()) #to lower case of string
print("this is to see the title method : ",string.title()) #to title case of string
print("this is to see the capitalize method : ",string.capitalize()) #to capitalize case of string
print("this is to see the swapcase method : ",string.swapcase()) #to swap case of string
print("this is to see the count method : ",string.count('l')) #to count of a character
print("this is to see the find method : ",string.find('l')) #to find a character
print("this is to see the replace method : ",string.replace('l','L')) #to replace a character
print("this is to see the strip method : ",string.strip()) #to remove whitespace
print("this is to see the split method : ",string.split()) #to split a string
print("this is to see the join method : ",string.join('l')) #to join a string
print("this is to see the isalpha method : ",string.isalpha()) #to check if a string is alphabetic
print("this is to see the isdigit method : ",string.isdigit()) #to check if a string is numeric
print("this is to see the isalnum method : ",string.isalnum()) #to check if a string is alphanumeric
print("this is to see the islower method : ",string.islower()) #to check if a string is lower
print("this is to see the isupper method : ",string.isupper()) #to check if a string is upper
print("this is to see the istitle method : ",string.istitle()) #to check if a string is title
print("this is to see the iscapitalize method : ",string.istitle()) #to check if a string is capitalize

#striing multiplication
strings = 'hello'
print("this is the original string :", strings)
print("this is to see the multiplication method : ",strings * 3) #to multiply a string

#Conditional Operators
number1 = 10
number2 = 20
print("number1 == number2 (number 1 is the same as number 2) : ",number1 == number2) #to check if two numbers are equal
print("number1 != number2 (number 1 is not the same as number 2) : ",number1 != number2) #to check if two numbers are not equal
print("number1 > number2 (number 1 is greater than number 2) : ",number1 > number2) #to check if the first number is greater than the second number
print("number1 < number2 (number 1 is less than number 2) : ",number1 < number2) #to check if the first number is less than the second number
print("number1 >= number2 (number 1 is greater than or equal to number 2) : ",number1 >= number2) #to check if the first number is greater than or equal to the second number
print("number1 <= number2 (number 1 is less than or equal to number 2) : ",number1 <= number2) #to check if the first number is less than or equal to the second number


#chained Conditional
a = 10
b = 20
c = 15
result1 = a == b
result2 = b > c
result3 = c < a + 2

result4  = result1 or result2
print("result1 or result2 (result1 or result2) : ",result4) #to check if result1 or result2 are true

result5 = result1 and result2
print("result1 and result2 (result1 and result2) : ",result5) #to check if result1 and result2 are true

result6 = not result1
print("not result1 (not result1) : ",result6) #to check if result1 is not true


#if else elif statement
nameif = input("Name :")

if nameif == "John"  :
    print("you're name is John")
elif nameif ==  "Tim" :
    print("You're name is Tim")
else : print("i dont know you're name")

