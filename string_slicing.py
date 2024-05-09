  # SLICING = CREATE A SUBSTRING BY EXTRACTING ELEMENTS FROM ANOTHER STRING 
   # we can do string slicing with basically to  functions ----
#  1. index[]   & 2. slice()
# 1. index[] ==>> [start:stop:step]

name = "Eman Gope"
first_name = name[0:3]  #NCOMPUTER ALWAYS TAKE THE FIRST INDICATOR AS ZERO ! 

print (first_name) # the result is Ema  not Eman .. WHY ?
# ANS ==>  Because the computer take the zero as an exclusive indicator nad the 3 as inclusive.
#           so whenever we are writing the [0:3 takinng the three spaces] ... it's just 
  
  # using of steps 

last_name = name[0:10:1]
print (last_name)

anohter_name= name[0:10:2]
print ( anohter_name)     # as the step is two it's just avoiding the next anme .. actually
                          # the steps are showing the next step.. it's 2 then it's collecting 
                          # second next step !

#  REVERSINNG THE STRING ==>>

reverse_name = name[::-1]   # (-1) step is used for reversing the string & there is no need to 
print (reverse_name)        # give the starting and ending index ....


                            #  slice() ==>> 

# slicing is same as the index operator !!!

website1 = "https://www.google.co.in/"
website2 = "https://www.freecodecamp.org/"

slice1 = slice(12,-7)  # instead of using : we are using , in skice function
slice2 = slice(12,-6)  #  string in python has two index -- 1. positive index .. it starts
                      # form 0 ... & 2. negative index .. its start form number (-1) 
                      # and conntinues along side decreasing its value ...

print (website1[slice1])
print (website2[slice2])