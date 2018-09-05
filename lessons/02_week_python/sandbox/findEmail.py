
# Find a name and email together
file = open("emails.txt")
for line in file:
    name, email = line.split(",")
    if name == "James Bond":
        print("  ** Found email: ",email)
