def fibsTuple(n):
    result = ( )
    a=1
    b=1
    for i in range(n):
        result += (a,)
        a, b = b, a + b
    return result

print(" My type is: ",type(fibsTuple))
print(fibsTuple(5)) #(1, 1, 2, 3, 5)
