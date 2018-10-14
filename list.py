# A demonstration of lists in Python
#

# lists are enclosed in square brackets, and all members do not
# need to be the same type
list1 = ['Alice', 'Bob', 500, ]

# display the items in the list
print ('The list has %d items' % (len(list1), ))
print ('%s' % (list1, ))
print ('The first item in the list is %r' % (list1[0], ))
for v in list1:
    print ('%r' % (v, ) )
print ('Does the list contain "Eve": %r' % ("Eve" in list1, ) )

list1[1] = 'Charlie'    # change the value of one of the list items
list1.append('Eve')     # add a new item to the list
del list1[0]             # delete the first item in the list

# display the items in the list (using the enumerate function so we also
# get the index for each iteration through the loop)
print ('\nThe list has %d items' % (len(list1), ))
print ('%s' % (list1, ))
print ('The first item in the list is %r' % (list1[0], ))
for (i, v) in enumerate(list1):
    print ('item %d: %r' % (i, v, ) )
print ('Does the list contain "Eve": %r' % ("Eve" in list1, ) )

