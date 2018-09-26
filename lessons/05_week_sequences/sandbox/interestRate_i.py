#!/usr/bin/env python3

def calcInterest(x0, p, N): # driver function
    # this finds the interest rates over a series of N years for rate p
    x_list = [] # this is a list of my yearly values of my loan

    print("  This is calcInterest, my driver function. ")
    x_list = [] #establish my list
    x_list.append(x0)
#    print("  My x_list is this :",x_list)
    for i in range(N): # for each year which is called 'N'

        lastElement = x_list[len(x_list) - 1]
#        print(" My list is this :", x_list)
        x = lastElement + (p/100) * lastElement
        x_list.append(x)

    return x_list
#end of calcInterest()

def saver(x_list):
    # save my results to a file for plotting later on...
    print(" This is the saver() function")
    fname = "rateValuesByYear.csv"
# convert the list to a string
    myData_str = "" #start wioth an empty string
    for i in range(len(x_list)):
        myData_str = myData_str + str(i) + "," +str(x_list[i]) + "\n"
#        print(" myData_str is", myData_str)
    f = open(fname,"w")
    f.write(myData_str)
    f.close()
    print("  Saver() saved the file to :", fname)
# end of saver()

def plotter(x_list):
# function to plot by results
    import matplotlib.pyplot as plt
    plt.plot(x_list,"ro")
    fname = "myRatePlot.png"
    plt.xlabel("Years")
    plt.ylabel("Value")
    plt.savefig(fname)
    plt.show()
#end of plotter()



# establish my input variable
x0 = 100000 # first payment on loan
p = 3.92 # interest rate
N = 6 # number of years of my loan.

#x_list = [] # this is a list of my yearly values of my loan
x_list = calcInterest(x0, p, N)
print("This is the root of the program, my x_list is the following :",x_list)
saver(x_list)
plotter(x_list)
