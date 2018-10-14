# A demonstration of exception handling in Python
#

# create an empty list
l = []

try:
    # we are going to attempt to access the first element of an empty list
    print('The first element in the list is %r' % (l[0], ) )
except Exception as e:
    # This raises an exception, which we catch and hadle here
    print('I caught an exception: %s (%s)' % (str(type(e)), str(e), ))

while len(l) < 3:
    # we can catch specific exceptions
    try:
        # attempt to get an integer from the user
        new_val = int(input('Enter an integer: '))
    except ValueError as e:
        # if they give us something we can't parse as an int then
        # we handle that specific exception (ValueError)
        print('That is not an integer - try again')
    else:
        # if no exception is raised, we can add the integer to the list 
        l.append(new_val)
    finally:
        # and whether an exception was raised or not, we show the contents
        # of the list after this iteration
        print('The list currently contains %s' % (str(l), ))




