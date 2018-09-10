n = 2.0 # the number from which to find square root.
guess = 1.0 # initial value for approx

print("  Initial values:  n = ",n, "guess = ",guess)

while abs(n - guess*guess) > .0001:
   #find  x_n - \frac{f(x_n)}{f'(x_n)}
   guess = guess - (guess*guess - n)/(2*guess)
   print("   *Current guess:   ",guess)
root = guess

print("   Result :",root)
