
# Find the summation of numbers in a textfile.
file = open("numbers.txt")
sum_int = 0 # defined outside of loop to be used inside and outside of loop 
for num in file:
    n_int = int(num) # convert string to an integer
    print(" Reading this number: ",n_int)
    sum_int = sum_int + n_int
print("  ** The summation of the above number is :", sum_int)

