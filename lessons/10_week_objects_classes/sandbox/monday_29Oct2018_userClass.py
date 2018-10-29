
# Date: 29 Oct 2018


class User:
    """This is a class to create a user object. Used to store name and birthday."""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        # Extract the first and last names
        name_pieces = full_name.split(" ") #ret a list
        self.first_name = name_pieces[0] # first element
        self.last_name = name_pieces[1] # second element
    #end of __init__()

    def age(self):
        """Return the age of the person in years. Convert birthday to get these years."""
        import datetime # library
        today = datetime.date(2018, 10, 29)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy,mm,dd) #date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)
#end of age()


#end of class

user = User("Frank Wright","08062018")#June 8, 1867
print(" ",user.name)
print(" ",user.first_name)
print(" ",user.last_name)
print(" ",user.birthday)
help(User) # print help concerning the class
