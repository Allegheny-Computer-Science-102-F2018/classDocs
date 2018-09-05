# Go line by line to find a name in a file
file = open("names.txt")
for line in file:
    print("  Reading this line: ",line)
    if line.startswith("James"):
        print("** Found the name: ",line)


