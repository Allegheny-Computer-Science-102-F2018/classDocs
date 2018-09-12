# date: 11 Sept 2018

# Ref: Saha, Chapter 1
# Saha, Amit. Doing Math with Python: Use Programming to Explore Algebra, Statistics, Calculus, and More!. No Starch Press, 2015.


'''
Unit converter: Miles and Kilometers
'''

def print_menu():
      print('1. Kilometers to Miles')
      print('2. Miles to Kilometers')
#end of print_menu()
def km_miles():
      km = float(input('Enter distance in kilometers: '))
      miles = km / 1.609
      print('Distance in miles: {0}'.format(miles))
#end of km_miles()
def miles_km():
      miles = float(input('Enter distance in miles: '))
      km = miles * 1.609
      print('Distance in kilometers: {0}'.format(km))
#end of miles_km
if __name__ == '__main__':
# executing this program directly runs it
# importing this code into another program will not prompt a menu
  print_menu()
  choice = input('Which conversion would you like to do?: ')
  if choice == '1':
          km_miles()
  if choice == '2':
          miles_km()
