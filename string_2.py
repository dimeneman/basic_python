'''
    To access individual characters within a string using the [] indexing notation.
    Note the character indices from 0 to n-1 , where n is the length of the string.
    We can accesss a part of string using by providing a [start:end] range instead 
    of a single index in [].
'''
my_name ='Eman Gope'
print(my_name)
print(len(my_name))

print(my_name[0])
print(my_name[8])

print(my_name[0:4]) # in python we've to take one extra index for the last index.....

# To check wheather a string contains some text , we've to use 'in' operator.
print('Gope' in my_name) # The output will be True...
print('bokachoda' in my_name)

'''
    Two or more strings can be joined using the + operator.Be careful while joining 
    strings , sometimes you may need to add a space character " " between words.
'''
greeting = 'Hello'
name = 'Rimni'
print( greeting + " " + name)

# There are some build in functions for sring which helps us to do certain operation...
new_name = 'BokaChoda'
# don't forget to give the ()
print(new_name.lower())   # it make all the letters lowercaase
print(new_name.upper())   # it makes all the letters uppercase
print(new_name.capitalize()) # it capatalize the first character and the rest is lowercase.
another_name = 'Eman Gope'
print(another_name.capitalize()) # it's also applicable even after space.

''' 
    The .replace method is used to replace a part of the string with another string . 
    it  takes the portion to be replaced and the replacement text as inputs or arguments.
'''
name_1 = name.replace('Rimni' , 'Soumya') # for replacing the element we need to input                                       
print(name_1)                             # the replacing part and after that we've to give the 
                                          # replacement part ...

'''
The (.split) method can be used to split a string into a list of strings based using the 
characters(s) provided.
'''                                     
example_1 = "Sun,Mon,Tue,Wed,Thu,Fri,Sat"
print(example_1.split(","))
