# A demonstration of dictionaries in Python
#

# dictionaries are enclosed in curly brackets, each member is a key/value pair
d = {'Alice': 98, 'Bob': 75, 'Charlie': 30}

# display the items in the dictionary
print ('The dictionary has %d items' % (len(d), ))
print ('%s' % (d, ))
for key in d:
    print ('%r: %r' % (key, d[key], ) )
print ('Does the dictionary contain "Eve" as a key: %r' % ("Eve" in d, ) )
print ('Does the dictionary contain 30 as a value: %r' % (30 in d.values(), ) )

d['Charlie'] = 100      # change the value of one of the items
d['Eve'] = 50           # add a new item
del d['Bob']             # delete one of the existing items

# display the items in the dictionary
print ('\nThe dictionary has %d items' % (len(d), ))
print ('%s' % (d, ))
for key in d:
    print ('%r: %r' % (key, d[key], ) )
print ('Does the dictionary contain "Eve" as a key: %r' % ("Eve" in d, ) )
print ('Does the dictionary contain 30 as a value: %r' % (30 in d.values(), ) )

