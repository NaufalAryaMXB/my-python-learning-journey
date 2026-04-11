#variables and data structure

name = "John" #string

age = 30 #integer

has_license = True #boolean

height = 5.9 #float

#print variables
print("Name:", name)
print("Age:", age)
print("Has License: ", has_license)
print("Height: ", height)

#user input
print('user Input')
nameinput = input("Name : ")
Ageinput = input("Age : ")
print("printing user input")
print("Name : ", nameinput)
print("Age : ", Ageinput)

#arithmetic operators
print("arithmetic operators")
num1 = 10
num2 = 20
print("num1 + num2 : ",int( num1 + num2)) #addition and force to  be integer
print("num1 - num2 : ", num1 - num2) #subtraction
print("num1 * num2 : ", num1 * num2) #multiplication
print("num1 / num2 : ", num1 / num2) #division
print("num1 % num2 : ", num1 % num2) #modulo
print("num1 ** num2 : ", num1 ** num2) #exponentiation
print("num1 // num2 : ", num1 // num2) #floor division

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

#list and tuples
#list is a collection of elements grouped together and they are mutable meaning they could  be changed 
list = [4, True, "Hi"] #this is a list identified by using [] 
print(len(list)) #len used to look at the length 
list.append('hello')  #add an elemnt   to the list
list.extend([4,5,"Heloo"]) #appends a another list into the the end  of the current list
list.pop() #delete an element at the end of the list
list.pop(0) #delete an element from the list depending on the index (starting from 0)
list[0] =  'Hello' #change an element depending on the index 

#tuple are similar to list but they are immuatble meaning they cannot be edited and uses ()
tuple = (0,3,2,2)
# tuple[0] = 5 # will error since tuple is immutable (commented out so the script doesn't crash)

#you can't edit tuple but you can add tuples into  list
listtuple = [5,"helo",(3,4,"Hello",[1,4,5,"hey"])]

#Loops
#for loops
for numbers in range(10):  #for loops  will loop if the rule is valid so  in   this case its 0-9  (10 not in cluded)
    print(numbers)

for numbers in range(5,10,2): #and the range function can  have a collection  based on the input we give it
                          #the input to range is (start,stop,step) (in this case its start:5,stop10,stesp2)  if only 1 input  that is stop if 2 inputs its start,stop
    print(numbers)

#While loops
i = 0
while i < 10: #while  loops as long as the condition is true it will  keep looping
    print("run")
    i += 1

dict = {'keys':4} #dict is a {key:value} to store data
dict['key2'] = 5 #add a new key  and value 
print("this is  print of full dict",dict) #to print the whole dict
print("this is  print of a single  key  ",dict["key2"])  #to pick a single value from a key
print('key2'  in dict) #to check if a key is inside
print(dict.values()) #just to see every value only  in the dict
print(list(dict.keys())) #just to see every key only  in the dict and  turning it into a list
del dict["key2"] #is to delete  a key and its  value
print(dict) 

sets
set = set()
s  =  {4,32,2,2}
s2 =  {3,4,22,1}
print(s)
s.remove(32) #to delete an element from a set
print(32 in  s) # to check if an element is inside the set
print("this  is  difference: ",s.difference(s2)) #to check the difference of  s and s2 or meaning telling everything in s that isnt  in s2
print("this  is  union:",s.union(s2)) #mash the two sets together
print("this  is  intersection:",s.intersection(s2)) #giving the element that both have
print("this  is  symmetric  difference:",s.symmetric_difference(s2))#mash the two together but delete the   one  that  both s and  s2 have


# Functions
# Functions allow you to bundle code into a reusable block so you don't have to rewrite the same math or logic.
def circle(r):
    L = (22/7) * r**2   # Calculate the area
    return L # 'return' gives the answer back to the code that called the function

user_radius = int(input("Enter radius number: "))
area_result = circle(user_radius) #it  will return here and 
print("Area of a circle with radius", user_radius, "is:", area_result)

Try and Except  
try:  #try lets you test a block  of code for errors
  print(x) #example here x is not defined
except: #cause an error accured it will print an exception
  print("An exception occurred")
#else
#the else lets you know if  no  error occurd
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")





