#!/usr/bin/env python3

# Date: 10 Sept 2019
# To run this program: python3 cars_ii.py
# Version : i

def redFunction():
    print("\n *redFunction() called")
    # called if "red" was entered at main()
    print("  User entered Red, the car was a Subaru!")
#end of redFunction()

def blueFunction():
    print("\n *blueFunction() called")
    # called if "blue" was entered at main()
    print("  User entered Blue, the car was a Toyota!")
# end of blueFunction()


def main(): # main function (driver)
    # ask the user what color car they saw
    msg = "  What color car did you see? (options: blue or red) : "
    color = str(input(msg))
    print("  The entered color is <<", color,">> and the type is", type(color))
    if color.upper() == 'BLUE': #helps with input: blue = BlUe = BLUE
        blueFunction() # call this function if "blue"
    elif color.upper() == 'RED':
        redFunction() #call this function is "red"
    else:
        print("  I do not know that car! :-(")
#end of main()

######  Begin the program by calling the function  #######
main() # start the program by calling the main() function.
