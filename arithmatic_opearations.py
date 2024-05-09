'''
 while performing arithmatic operations , integers are automatically converted
 to floats if any of the operands is float . Also , the divison operator  /  always 
 returns a float . Even if both operands are integers . Use the // operator if you want
 the result of division to be an int.
'''
print(type( 45*3.0 ))
print(type( 45*3 ))

result_1=(10/3)
print(result_1)
print(type(result_1))

# for printing only the integer part we've to use the '//' this sign ...

result_2 = (10//3)
print(result_2)
print(type(10//3))
