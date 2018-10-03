#!/usr/bin/env python3

# Note: In terminal, type in "chmod +x program.py" to make file executable

"""calcTruth.py  A demo to show how lists can be used with functions to make boolean calculations"""

__author__      = "Oliver Bonham-Carter"
__date__        = "3 October 2018"


def myAND(in1_bool, in2_bool):
# function to determine the boolean AND calculation.
    return in1_bool and in2_bool

#end of myAND()


def myOR(in1_bool, in2_bool):
# function to determine the boolean OR calculation.
    return in1_bool or in2_bool

#end of myOR()

def main(): # lead function
#define the list of true and false values

    A_list = [True, True, False, False]
    B_list = [True, False, True, False]
    print(" Welcome to the CalcTruth program!")
    truth_dic = {}
    for a in A_list:
        for b in B_list: 
#            print("  Current values, a = ",a,"b = ",b)
            myOR_bool = myOR(a,b)
            myAND_bool = myAND(a,b)

            truth_dic[str(a)+" OR "+str(b)] = myOR_bool
            truth_dic[str(a)+" AND "+str(b)] = myAND_bool

    for i in truth_dic:
        print("  ",i, ":", truth_dic[i])
    print(" All finished!")
#end of main()

main() # driver function


