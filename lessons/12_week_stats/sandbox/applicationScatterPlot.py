#Scatter Plot Code

import matplotlib.pyplot as plt

def scatter_plot(x, y):
 plt.scatter(x, y)
 plt.xlabel('Grades')
 plt.ylabel('Test Scores')
 plt.show()


 #High_School_Grades_list
x = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
 #College_Admin_Tests_list
y = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]

scatter_plot(x,y)
