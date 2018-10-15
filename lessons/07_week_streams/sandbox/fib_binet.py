import math
def fibsBinet(n):
    a = (1/math.sqrt(5))
    b = ((1 + math.sqrt(5))/2)**n
    c = ((1 - math.sqrt(5))/2)**n
    return a * (b - c)
#end of fibsBinet()

for i in range(20):
    print(fibsBinet(i)) # calculate each value as needed
