today = "Subnday"
print(type(today))

new_movie = 'Welcome to Akash\'s  house'   '''
                                              If we have to use single quotation but 
                                               beacuse of the syntax error we are unable to
                                               do it . To solve this problem we can easily 
                                               add an backslash and then we can do it .  
                                               Or , we can use a double quotation .
                                               We can also use alternative.
                                            '''

# For a multilinne string we use tripple quotation....

long_text = """ Are you new to open source and want to learn more about 
                some interesting projects that you can contribute to? 
                Join GSoC where mentors will help guide you on your journey """

print(long_text)

''' 
   The (len) function will help us the find the number of characters in the string variable.
   The string is also a container that's why the (len) function is usable
 '''
print(len(long_text))

print('a\nb') # \n character helps us to create a new line..it also count as a character.

print(len('a\nb')) 
'''Note that spsecial characters like '\n' and escaped characters like \" count as a
   single character , even though they written and sometimes printed as 2 characters.
'''
