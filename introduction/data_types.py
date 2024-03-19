#Numeric data types
a=100
b=32
c=3.14
print(a+b*2)
print((a+b)*2)
print(a==b)
print(a>b)
print(a<b)
print(a!=b)
d=12+2j
print(a+b+c+d)#python sequence data type
    #sequence is a collection of ordered data types
    #these are>>>>>>string data type (Non-numeric data type)
    #The plus(+), concatenation operator "+" can be used to combine two strings  
    #Example: print("Hello" + "World")  #output Hello World
    
    #list data type
                    #tuple data type
                    #set data type
plp_str="welcome to PLP Academy"
print(plp_str)
print(plp_str[0])
print(plp_str[-1])
print(plp_str[10:15])#from index 10 to 15
print(len(plp_str))#number of characters in the string
student_str ='python Class'
tuple=('abcd',786,2.25,'john',70.2)
tinytuple=123,5+6j,'john'
print(tuple)
print(tuple[2:3])#from second element to third element
print(tuple+tinytuple)
print(tinytuple*3)
dict={}
dict['one']="This is one"
dict[2]="This is two"
tinydict={'name':'jone','code':6734,'dept':['sales']}
print(dict)
print(dict['one'])
print(tinydict)
print(tinydict.keys( ))#returns all keys present in dictionary
print(tinydict.values())#returns values of dictionary
print(tinydict.items() )# returns key and value pairs from dictionary 

