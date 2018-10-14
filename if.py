# A demonstration of if statements in Python
#

s1 = input('Enter the 1st string: ')
s2 = input('Enter the 2nd string: ')
# if you are using python 2.x, replace the 2 lines above with the 2 lines below
#s1 = raw_input('Enter the 1st string: ')
#s2 = raw_input('Enter the 2nd string: ')

# Standard if/else if/else statement.  There can be zero of more elif clauses
# and 0 or 1 else clause at the end.  Note that the indentation is required
# to define the body of each if clause (as opposed to being optional in C++)
if s1 == s2:
    print ("The strings are the same")
elif s1 > s2:
    print ("Alphabetical ordering is %s, %s" % (s2, s1, ) )
else:
    print ("Alphabetical ordering is %s, %s" % (s1, s2, ) )

if s1 == 'Hello' and s2 == 'World':
    print ('You guessed the magic phrase!')


