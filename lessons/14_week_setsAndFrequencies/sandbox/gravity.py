# date: 27 Nov 2018

# Saha, page 130

from sympy import FiniteSet, pi
def time_period(length, g):
    T = 2*pi*(length/g)**0.5
    return T
#end of time_period()
if __name__ == '__main__':
    L = FiniteSet(15, 18, 21, 22.5, 25) #define the lengths as sets
    g_values = FiniteSet(9.8, 9.78, 9.83) #define three gravity values in a set
    print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)'))
    for elem in L*g_values: # the cartesian product
        l = elem[0]
        g = elem[1] #take defined number
        t = time_period(l/100, g)
#        print("\n",elem)
        # output the gravity values in triplicate
        print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l), float(g), float(t)))
