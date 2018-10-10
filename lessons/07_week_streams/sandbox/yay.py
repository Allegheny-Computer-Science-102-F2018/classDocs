
def my_gen():
    # function to act as a generator
    n = 1
    print(" This is my first statement.")
    # generator statement
    yield n # place this value into memory until needed

    n += 1 #means this: n = n + 1
    print(" This is my second statement.")
    yield n

    n += 1
    print(" This is my third statement.")
    yield n

#end of my_gen()


a = my_gen() # leading generator function
print(" Type of a-variable is: ",type(a))

next(a) #Gimme the first yield statement
next(a) #Gimme the second yield statement
next(a) #Gimme the third yield statement
#next(a) #Gimme the another yield statement??

# do the math in the my_gen()
# use a loop to iterate
for i in my_gen():
 print("mygen() :",i)

