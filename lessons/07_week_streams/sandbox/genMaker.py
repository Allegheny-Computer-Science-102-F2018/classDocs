def fibs(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a, b = b, a + b
print([x for x in fibs(6)])
print(" My type is:",type(fibs))
f = fibs(6)
for i in f: print(i)
print(" My type is: ",type(fibs(6)))
