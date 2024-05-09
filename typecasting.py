x = 5 # int 
y =  8.7 # float
z = "3"  # string 

print (x)
print (y)
print (z)

# if we want to change the daatatype of the code we have to use typecasting 

print (int(y))  # as we can see the float value is converted into an integer value
print (int(z))
print (float(y))
print (str(y))

# now the above changes are temporary , for making it permanent we have
# to change the value into the required datatype 

y = int(y)
print (y)

z = float (z)
print (z)

# why do we need typecasting ?
# Ans ==>>  we can't perform mathematical operations with string and we have to 
#           make it into a integer value .... 
#           we can't use differenrt datatypes into a single print()  
#           particularly for this we need to perform typecasting !!

#print ("The value of x is " + x)  --->> this code is wrong because of various datatypes 
# the write code is
print ("The value of x is " + str(x))