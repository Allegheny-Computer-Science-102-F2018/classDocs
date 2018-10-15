def fibsList(n):
    result = [ ]
    a=1
    b=1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
print(" My type is: ",type(fibsList))
print(fibsList(5)) #[1, 1, 2, 3]
