# A demonstration of arithmetical operations in Python
#

val1 = int(input('Enter the 1st value: '))
val2 = int(input('Enter the 2nd value: '))
# if you are using python 2.x, replace the 2 lines above with the 2 lines below
#val1 = int(raw_input('Enter the 1st value: '))
#val2 = int(raw_input('Enter the 2nd value: '))

print('%d + %d = %d' % (val1, val2, val1 + val2, ) )
print('%d - %d = %d' % (val1, val2, val1 - val2, ) )
print('%d * %d = %d' % (val1, val2, val1 * val2, ) )
print('%d / %d = %d' % (val1, val2, val1 / val2, ) )
print('%d ** %d = %d (x to the power of y)' % (val1, val2, val1 ** val2, ) )
print('%d // %d = %d (Integer Division)' % (val1, val2, val1 // val2, ) )
print('%d %% %d = %d (Modulus)' % (val1, val2, val1 % val2, ) )




