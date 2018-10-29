
# Date: 29 Oct 2018


class Family(): #create class
    pass # class does nothing
#end of class Family

myPals = Family() #instance of object


myPals.f_name00 = "Alexander"
myPals.l_name00 = "Banhom-Certar"

myPals.f_name01 = "Daisy"
myPals.l_name01 = "Conham-Barter"

print(" Call the class for the first time")
print(" name from class: ", myPals.f_name00, myPals.l_name00)
print(" name from class: ", myPals.f_name01, myPals.l_name01)

f_name00 = "Johnny"
l_name00 = "Appleseed"

print(" name: ", f_name00, l_name00)

print(" Call the class for the second time")
print(" name from class: ", myPals.f_name00, myPals.l_name00)
print(" name from class: ", myPals.f_name01, myPals.l_name01)

print("________________________")
myPals.film00 = "Frozen"
myPals.hates_in_winter01 = "Snow"

print(myPals.f_name00,"and", myPals.film00)
#print(myPals.f_name01,"and", myPals.film01) #attribErr!
print(myPals.f_name01,"and", myPals.hates_in_winter01)
