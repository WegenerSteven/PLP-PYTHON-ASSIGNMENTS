
"""#TYPE CONVERSION
#Python Implicit Type conversion......python automatically converts one data type to another.
integer_num=123
float_num =1.23
new_num =integer_num + float_num
#display new value and resulting data type
print("Value:",new_num)
print("Data Type:",type(new_num)) 

#Explicit Type Conversion.....Users converts the data type of an object to the required data type
#We use built-in function like int(), float(), str(), etc to perform explicit type conversion


num_string='12'
num_integer=23
print("Data type of num_string before Type Casting:",type(num_string))
#explicit type conversion
num_string=int(num_string)
print("Data type of num_string after Type Casting:",type(num_string))
num_sum=num_integer+num_string
print("sum:",num_sum)
print("Data Type of num_sum:",type(num_sum))"""
    #Printing output and creating User Input in Python
#use print() function
print('Good Morning')
print('It is sunny today')

#print with end whitespace
#print('Good Morning!',end= '')
#print('It is rainy today')
print('PowerLP is'+' awesome')

#input() Function - used to get user input from keyboard
user_name=input("Enter your name: ")
age=input("Enter your age: ")
weight=input("Enter your weight: ")

#print user details
print("\nHello,",user_name,"\nYou are "+age+ " years old.")
if int(age)>18:
    print("You can vote.")
else:
    print("Sorry you cannot vote yet.")