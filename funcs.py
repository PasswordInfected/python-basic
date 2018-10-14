# A demonstration of functions in Python
#

# importing a module
import random

# define a function that takes no arguments, and just prints a message
def showMessage ():
    print ('Hello from showMessage(), a boring function!')

# define a function that takes a single argument, and returns a value
def square (n):
    return n * n

# define a function that takes two optional arguments, and returns
# a random integer in that range [a, b].  Note the use of default
# values for the arguments to be used if they are not provided in the call
def getRand (a = 1, b = 10):
    print('getRand function with args a = %d and b = %d' % (a, b, ))
    return random.randint(a, b)

# a function that changes the value of a parameter
def changeList (l):
    print('changeList - at the start l = %s' % (l, ))
    # change each of the current values
    for i in range(0, len(l)):
        l[i] = l[i] * 10
    # and add a new value at the end
    l.append(l[-1] * 10)
    print('changeList - at the end l = %s' % (l, ))



# call the most basic function
showMessage()

# now call the square function
val = int(input('\nEnter an integer: '))
print('%d squared = %d' % (val, square(val), ))

# call the rand function without parameters
r_val = getRand()
print('A random value from getRand with no params: %d\n' % (r_val, ))

# call the rand function with both parameters
r_val = getRand(20, 30)
print('A random value from getRand with both params: %d\n' % (r_val, ))

# call the rand function with one named parameter
r_val = getRand(b = 40)
print('A random value from getRand with one named param: %d\n' % (r_val, ))

# call the function that changes the value of the parameter
my_list = [1, 2, 3, ]
print('\nBefore call changeList, my_list = %s' % (my_list, ))
changeList(my_list)
print('After call changeList, my_list = %s' % (my_list, ))



