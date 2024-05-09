'''A dictionary is an unordered collection of items . Each item stored in a dictionary
   has a key and value . Keys are used to retrive values from the dictionary . Dictionaries 
   have the type 'dict'
.
                      Dictionarries often used to used store many pieces of information
e.g. details about a person , in a single variable . Dictionaries are created by enclosing 
key-value pairs within curly brackets { and }.
'''

person_1 = { 'name' : 'Soumyadeep Das',
             'sex': 'Randi' ,
             'age': 19 ,
             'staus': 'nunkubihin' ,
             'married':'False' }
             
print(person_1)

# Dictionaries can also be created using the dict function..
person_2 = dict(name ='Subhradeep kundu', sex ='male' , age = 19 , status = 'choto_nunku')
print(person_2)

print(type(person_1)) , print(type(person_2))

# keys can be used to access values using square brackets [ nad ]
print(person_2['name'])
print(person_1['name'])


''' the 'get' method also accepts a default value which is returnd if the key isn't
    present int the dictionary.
'''
person_3 = person_2. get('address','unknown') # for this we've to store the value in 
                                              # another variable...
print(person_3)


# using the assignment operator we can change the value associated with a key
person_1['married'] = 'True'
print(person_1)

# The asignment operator can also be used to add new key-value pairs to the dictionary.
person_1['address'] = 'Lowada'
print(person_1)

# To remove a key and the associated value from a dictionary , use hte 'pop' method...
print(person_1.pop('address'))  # it will gives us the value according to the key ...



print(person_2.keys())        # it will give us only the keys

print(person_2.values())      # it will give us only the values 

print(person_2.items())       # it will give the pair of ( 'key' , 'value' )
