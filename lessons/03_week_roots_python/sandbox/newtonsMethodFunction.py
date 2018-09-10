
def NM(n, guess):
    print("  Initial values:  n = ",n, "guess = ",guess)

    while abs(n - guess*guess) > .0001:
        #find  x_n - \frac{f(x_n)}{f'(x_n)}
        guess = guess - (guess*guess - n)/(2*guess)
        print("   *Current guess:   ",guess)
        root = guess
    return root
#end of NM()
#get parameters to call function NM()
n = 2 # the number from which to find square root.
guess = 1.0 # initial value for approx
print(" Finding root : ",n)
print(" Approx guess : ", guess)
print("  Result : ",NM(n, guess))
