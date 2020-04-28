name='Mikey'
surname='Basuki'
print('Hi,', name, surname, '! \n')

# Python program to print prime factors 

import math 

# A function to print all prime factors of 
# a given number n 
def primeFactors(n):

    # Print the number of two's that divide n
    pow2 = 0
    while n % 2 == 0:
        #print (2),
        pow2 = pow2 + 1
        n = int(n / 2)

    if pow2 > 0:
        print('2 ^',pow2)
        print("After dividing by 2's,", 'the odd remaining dividend is',n)
        sq = int(math.sqrt(n))
        print('Square root of', n, 'is about', sq)

    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used
    s = 0
    for i in range(3,int(math.sqrt(n))+1,2):

        pow = 0
        # while i divides n , print i and divide n
        s = s + 1
        while n % i == 0: 
            #print (i),
            pow = pow + 1
            n = int(n / i)

        if pow > 0:
            print(i, '^',pow)
            
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print (n, '^ 1'),

    print(s,'iterations for odd number.')
        
# Driver Program to test above function 

strn = input("Type the number: ")
n = int(strn)
print('n =',n)
sq = int(math.sqrt(n))
print('Square root of', n, 'is about', sq)
print('The prime factor(s) of',n,'are:')
primeFactors(n)
input('Press ENTER to exit')
# This code is contributed by Harshit Agrawal 
