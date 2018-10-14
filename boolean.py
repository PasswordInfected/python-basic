# A demonstration of comparison and boolean operations in Python
#

val1 = int(input('Enter the 1st value: '))
val2 = int(input('Enter the 2nd value: '))
# if you are using python 2.x, replace the 2 lines above with the 2 lines below
#val1 = int(raw_input('Enter the 1st value: '))
#val2 = int(raw_input('Enter the 2nd value: '))

# basic comparison operators
print('%d == %d = %r' % (val1, val2, val1 == val2, ) )
print('%d != %d = %r' % (val1, val2, val1 != val2, ) )
print('%d > %d = %r' % (val1, val2, val1 > val2, ) )
print('%d >= %d = %r' % (val1, val2, val1 >= val2, ) )
print('%d < %d = %r' % (val1, val2, val1 < val2, ) )
print('%d <= %d = %r' % (val1, val2, val1 <= val2, ) )

# bitwise operators (output as boolean to see results more clearly)
print('\n%s | %s = %s (BITWISE OR)' % (bin(val1), bin(val2), bin(val1 | val2), ) )
print('%s & %s = %s (BITWISE AND)' % (bin(val1), bin(val2), bin(val1 & val2), ) )
print('%s ^ %s = %s (BITWISE XOR)' % (bin(val1), bin(val2), bin(val1 ^ val2), ) )
print('~%s = %s (BITWISE NOT)' % (bin(val1), bin(~val1), ) )

# boolean operators
a = True
b = False
print('\n%r and %r = %r (BOOLEAN AND)' % (a, b, a and b, ) )
print('%r or %r = %r (BOOLEAN OR)' % (a, b, a or b, ) )
print('not %r = %r (BOOLEAN NOT)' % (a, not a, ) )

