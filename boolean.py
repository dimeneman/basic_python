# Boolean represent one of 2 values : 'True' & 'False' . Booleans have the type bool.

is_today_sunday = True
print(type(is_today_sunday))

is_today_monday = False
print(type(is_today_monday))

# Booleans are generally returned as the result of a comparison operation (e.g.== , >= etc.)

my_favourite_number = int(input()) # taking input
print("my enterd number is" ,my_favourite_number)

if my_favourite_number > 0 and my_favourite_number <= 3:
 print('True')
else:
 print('False')

'''
Booleans are automatically converted to int , when used in arithmatic operatioiins.
True = 1 and False = 0.
 ''' 
sum_1 = (5 + False)
print(sum_1)

sum_2 = (5 + True)
print(sum_2)

# boolean values can be converted into 0 & 1 easily 
# for False 

try_1 = bool(False)
print(try_1)
try_2 = bool(0)
print(try_2)
try_3 = bool(0.0)
print(try_3)
try_4 = bool(None)
print(try_4)
try_5 = bool("")
print(try_5)
try_6 = bool([])
print(try_6)
try_7 = bool(())
print(try_7)
try_8 = bool({})
print(try_8)
try_9 = bool(set())
print(try_9)
try_10 = bool(range(0))
print(try_10)

# for True || Any real values including set , list , string (not empty) can be considered as True by bool function

new_1 = bool(True)
print(new_1)
new_2 = bool(1)
print(new_2)
new_3 = bool(2.0)
print(new_3)
new_4 = bool("hello")
print(new_4)
new_5 = bool ([1,2])
print(new_5)
new_6 = bool((1,2))
print(new_6)
