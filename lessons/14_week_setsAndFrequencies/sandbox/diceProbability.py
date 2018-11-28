# date: 27 Nov 2018

# Saha, page 132

def probability(space, event):
         return (1.0 * len(event))/len(space)
         # the 1.0 is used to convert floats in python2
#end of probability()



def check_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True
#end of check_prime()

from sympy import FiniteSet

if __name__ == '__main__':
    space = FiniteSet(*range(1, 21)) # store sample space
    primes = []
    for num in space:
        if check_prime(num): # is this number a prime
            primes.append(num) # make a list of the primes
    event = FiniteSet(*primes)
    p = probability(space, event) # calculate probability
    print('Sample space: {0}'.format(space))
    print('Event: {0}'.format(event))
    print('Probability of rolling a prime: {0:.5f}'.format(p))
