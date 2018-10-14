# A demonstration of input in Python
#

name = input('What is your name: ')
# if you are using python 2.x, replace the line above with the line below
#name = raw_input('What is your name: ')

print("Hello %s, we're going to add some numbers!" % (name, ))

val1 = int(input('Enter the 1st value: '))
val2 = int(input('Enter the 2nd value: '))
# if you are using python 2.x, replace the 2 lines above with the 2 lines below
#val1 = int(raw_input('Enter the 1st value: '))
#val2 = int(raw_input('Enter the 2nd value: '))
sum = val1 + val2

print('%d + %d = %d' % (val1, val2, sum, ) )




