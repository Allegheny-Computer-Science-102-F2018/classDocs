#!/usr/bin/env python3



class User:
    """This is a class to create a user object. Used to store name aband birthday."""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        # Extract the first and last names
        name_pieces = full_name.split(" ") #ret a list
        self.first_name = name_pieces[0] # first element
        self.last_name = name_pieces[1]  # second element
    #end of __init__()
#end of class


    def ageMethod1(self):
        """Return the age of the person in years. Convert birthday to get these years."""
        today = datetime.date(2018, 10, 29)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy,mm,dd) #date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)
        #end of age()

    def getToday(self):
        """returns today's data in yyyy-mm-dd format"""
        import datetime #library
        today = datetime.datetime.today().strftime('%Y-%m-%d') # On one line. Is a string
        yyyy = int(today[0:4])
        mm = int(today[5:7])
        dd = int(today[8:10])
        today = datetime.date(yyyy,mm,dd) #date of birth
        return today
        #end of getToday()

    def ageMethod2(self):
        """Return the age of the person in years. Convert birthday to get these years."""
        yyyy_b = int(self.birthday[0:4])
        mm_b = int(self.birthday[4:6])
        dd_b = int(self.birthday[6:8])
         #date of birth
        dob = datetime.date(yyyy_b,mm_b,dd_b)
        today = self.getToday()
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)
        #end of age()



import datetime # library
user = User("Frank Wright","18670608") # Make instance for Frank, June 8, 1867
print("    FullName: ",user.name)
print("       First: ",user.first_name)
print("        Last: ",user.last_name)
print("    Birthday: ",user.birthday)
print("  AgeMethod1: ",user.ageMethod1()) # old technique
#print("  AgeMethod2: ",user.ageMethod2()) #dynamic date getting


#create another instance of this object with a new name

#user1 = User("Franky Wrighty","20170608") #June 8, 1867
#print("    FullName: ",user1.name)
#print("       First: ",user1.first_name)
#print("        Last: ",user1.last_name)
#print("    Birthday: ",user1.birthday)
#print("  AgeMethod1: ",user1.ageMethod1()) # old technique
#print("  AgeMethod2: ",user.ageMethod2()) #dynamic date getting

#help(User)
