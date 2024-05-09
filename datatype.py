'''
 The datatypes in python are - int , str , float , bool, none , list , tuple , dictionry
 we can define datatypes by using the type function !
 '''

year = 2020
print(type(year))  # int in python include all the positive and negative value .

percentage = 96.67
print(type(percentage))  # float includes all the decimal numbers(positve and negative both nummbers)

word = 'eman'
print(type(word))    # character and string datatype is same in python 

a_number = 3.0
print(type(a_number))  # a whole number with a decimal point is treated as a float in python


''' floating point numbers can  also be written using the scientific notataion with an "e"
 to indicate the power of 10.
 '''

one_by_thousand = 1e-3
print(one_by_thousand)
print(type(one_by_thousand))

avogardo_number = 6.022e-23
print(avogardo_number)
print(type(avogardo_number))

# float , int these datatypes can  be used as a function to convert eachother

number_float = 1.333
number_int =int(number_float)
print(number_int)


'''
The NoneType includes a single value None , used to indicate the absence of a value.
None has the NoneType . It is often used to declare variable whose value may be 
assigned later.
'''
nothing = None
print(type(nothing))
