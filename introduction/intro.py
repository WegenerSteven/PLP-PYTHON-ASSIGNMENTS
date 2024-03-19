#print("Hello World")
languages = ["Swift", "Java","python"]
# To access element at index 0
print(languages[0])
print(languages[2])
print(languages[1])
print(type(languages))
#Tuple>>>>>is an ordered sequece of items same as list.
#The difference is (tuples are immutable)
#we use parenthesis() to store items of a tuple.
#tuples once created cannot be modified
product = ('Xbox',499.99)
#similar to lists we use the index number to access tuple items in python
product = ('Microsoft','Xbox',499.99)
print(product[0])
print(product[1],product[2])
print(type(product))
#python string data type
          #string is a sequence of characters represented by either single or double quotes.
name = 'python'
print(name)
message='python for beginners'
print(message)
print(type(message))
#python set data types
         #set is an unordered collection of unique items. 
         #set is defined by values separated by commas inside braces{}. 
student_id = {112, 114, 116, 118, 115}
print(student_id)#display student_id elements
print(type(student_id)) #display type of student_id

#python dictionary data type
        #python dictionary is an ordered collection of items.
        #it stores elements in key/value pairs. 
capital_city = {'Nepal': 'Kathmandu','Italy':'Rome','England':'London'}
print(capital_city)
    #keys are >> 'Nepal', 'Italy', 'England'
    #values are >> 'Kathmandu', 'Rome', 'London'
print(capital_city['England']) #we use keys to retrieve the respective value.
