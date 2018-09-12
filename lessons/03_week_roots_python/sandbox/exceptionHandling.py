
print("Exeption handling...")
try:
    a_int = int(input("  Enter an int, not a string  :"))
except ValueError:
    print("  Cannot convert string to int or float...")
