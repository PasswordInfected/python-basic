# A demonstration of loops in Python
#

s = input('Enter a string: ')
n = int(input('Enter an integer: '))
# if you are using python 2.x, replace the 2 lines above with the 2 lines below
#s = raw_input('Enter a string: ')
#n = int(raw_input('Enter an integer: '))

# basic counting for loop
for i in range(n + 1):
    print(i)

# iterate through string characters using index
for i in range(len(s)):
    print(s[i])

# we can also iterate through characters using this format
for c in s:
    print(c)

# example of a while loop
correct = 5
done = False
while not done:
    guess = int(input('Guess a number between 1 and 10: '))
    done = (guess == correct)
    if not done:
        print ("That's not correct - try again!")


