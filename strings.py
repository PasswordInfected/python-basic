# A demonstration of string operations in Python
#

s1 = input('Enter the 1st string: ')
s2 = input('Enter the 2nd string: ')
# if you are using python 2.x, replace the 2 lines above with the 2 lines below
#s1 = raw_input('Enter the 1st string: ')
#s2 = raw_input('Enter the 2nd string: ')

print('"%s" has %d characters' % (s1, len(s1), ))

print('"%s" + "%s" = "%s"' % (s1, s2, s1 + s2, ))
print('"%s" * 3 = "%s"' % (s1, s1 * 3, ))
print('"%s"[0] = "%s" (GET FIRST CHARACTER)' % (s1, s1[0], ))
print('"%s"[2] = "%s" (GET THIRD CHARACTER)' % (s1, s1[2], ))
print('"%s"[2:5] = "%s" (SLICE - GET 3rd-5th SUBSTRING)' % (s1, s1[2:5], ))
print('"%s"[:5] = "%s" (SLICE - GET 1st-5th SUBSTRING)' % (s1, s1[:5], ))
print('"%s"[-1] = "%s" (SLICE - GET LAST CHAR)' % (s1, s1[-1], ))
print('"%s"[-5:] = "%s" (SLICE - GET LAST 5 CHAR SUBSTRING)' % (s1, s1[-5:], ))

print('Does "%s" start with "%s": %s' % (s1, s2, s1.startswith(s2), ))
print('Does "%s" end with "%s": %s' % (s1, s2, s1.endswith(s2), ))
print('Does "%s" contain "%s": %s' % (s1, s2, s2 in s1, ))
print('Does "%s" not contain "%s": %s' % (s1, s2, s2 not in s1, ))



