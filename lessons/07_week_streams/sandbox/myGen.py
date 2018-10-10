def createGenerator():
    mylist = range(3) # a list is created od lengh 3
    for i in mylist:
    # find the square of the value as needed
        yield i*i
# end of createGenerator()

###################

# Initiation: create a generator
myGenerator = createGenerator()
# Where is this generator in memory?
print(myGenerator) # print the memory address where the gen is held
print(type(myGenerator))
for i in myGenerator: # go back to the generator and perform the calculation
    print(i)
