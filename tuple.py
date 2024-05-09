''' A tuple is an oredered collection of values , similiar to list , however it's
     not possible to add , remove or modify values in a tuple. A tuple is created by 
     enclosing values within parantheses ( and ) , separated by commas.
'''
''' Any data structure that cannot be modified after creation is called immutable .
Tuple is also a immutable lists. (consideerable) & that's the differnces between lsits 
lists and tuple...
'''

fruits = ('apple' ,'orange','watermelon')
print(fruits)

print(len(fruits))            # list of the element
print(fruits[0])              # accesing a particular element (same as list)

fruits[0] = 'avacado' # this line will gives us errore because tuple can't be changed !
# we can also not be able to use 'append' & 'remove' method
# we can convert tuple to lists and lsits to tuple.


# list to tuple                       // for runnig the code look at line 16
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)


# tuple to list
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)


