#!/usr/bin/env python3
 # note: type in "chmod +x myTruthTable.py" to make self-executable


def myAND(in1_bool, in2_bool): #function to return the AND of two inputs
    print(" Input to AND: ",in1_bool,"::",in2_bool)

    result = in1_bool and in2_bool
    print("   AND Result is :",result)
#end of myAND()


def myOR(in1_bool, in2_bool): #function to return the OR of two inputs
    print(" Input to OR: ",in1_bool,"::",in2_bool)

    result = in1_bool or in2_bool
    print("   OR Result is :",result)
#end of myOR()


def main(): # driver function

    #establish some lists of data: columns of data for truth table
    A_list = [True, True, False, False]
    B_list = [True, False, True, False]

    for a in A_list:
#        print(" My A_list term is :",a)
        for b in B_list:
#                print(" My B_list term is: ", b)
                myAndOutput_bool = myAND(a, b)

    for a in A_list:
#        print(" My A_list term is :",a)
        for b in B_list:
#                print(" My B_list term is: ", b)
                myAndOutput_bool = myOR(a, b)



#end of main()



main() # driver function
