''' A list in python is an ordered collection of values . Lists can hold values of
 different datatypes , and support to add , remove and change values . Lists have the 
 type 'list'
'''
fruits = ['apple', 'mango','lichhi',7,True] 
print(fruits)
print(type(fruits))

empty_list = [] 
print(len(fruits)) # there are 5 elements in fruits lsit .

# To  get access the elements of a list using the index od the element,starting
# from the index 0....

fruits[0] # now we've the access of  'apple'
print(fruits[0]) # now this will print apple
print(fruits[1]) #now this will print mango

# we can also access the elements of the list by negative value..in this method the 
# last element's index should be -1
print(fruits[-1])
print(fruits[-2])

# we can also add another list inside of a list , it will be a subset

new_list = ['eman','soumya','bokachoda',1,['amrit','harsh','ayush']]
print(new_list)

# to get acces for some sepecific elements we need to give it's range
print(new_list[2:5])   # we've to remember the ending range should be (n+1) if we want 
                       # to print the nth term....

# A new element  can be add to the end of the lsit by usinng the append method
new_list.append('subhra')
print(new_list)

# A new value can aslo be inserted a specific index using the "insert" method.
new_list.insert(1,'subhra')
print(new_list)

# to remove a particular element from a element we've use the "remove" method

new_list.remove('eman')
print(new_list)

# now if we've to remove the value by index then , we've to use the "pop" method 
new_list.pop(1)
print(new_list)

print('dev' in fruits)

# to combine two or more list we need to use the '+' operator ...
fruit_1 = ['mango','guava','pineapple']
fruit_2 = ['lichi','waermelon','apple']
fruit_3 = ['tomato','orange','grapes']
more_fruits = fruit_1 + fruit_2 + fruit_3 
print(more_fruits)
