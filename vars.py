# A demonstration of the use of variables in Python
#

# string and int variables
name = "Alice"
grade = 98

# two ways to display the same information
print (name + ' scored ' + str(grade) + ' on the exam')
print ('%s scored %d on the exam' % (name, grade, ) )

# now let's change the type of grade
grade = 'A'
print ('The grade for %s was %s' % (name, grade, ) )





