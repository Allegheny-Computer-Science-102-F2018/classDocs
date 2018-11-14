def find_corr_x_y(x,y):
       n = len(x)
       # Find the sum of the products
       prod = []
       for xi,yi in zip(x,y): # the zip function
           prod.append(xi*yi)
       sum_prod_x_y = sum(prod)
       sum_x = sum(x)
       sum_y = sum(y)
       squared_sum_x = sum_x**2
       squared_sum_y = sum_y**2
       x_square = []
       for xi in x:
           x_square.append(xi**2)
       # Find the sum
       x_square_sum = sum(x_square)
       y_square=[]
       for yi in y:
           y_square.append(yi**2)
       # Find the sum
       y_square_sum = sum(y_square)
# Use formula to calculate correlation
       numerator = n*sum_prod_x_y - sum_x*sum_y
       denominator_term1 = n*x_square_sum - squared_sum_x
       denominator_term2 = n*y_square_sum - squared_sum_y
       denominator = (denominator_term1*denominator_term2)**0.5
       correlation = numerator/denominator
       return correlation
#end of find_corr_x_y(x,y)

simple_list1 = [1,2,3]
simple_list2 = [4,5,5]
result = find_corr_x_y(simple_list1,simple_list2)
print(" Set1:",simple_list1)
print(" Set2:",simple_list2)
print(" Correlation :",result)
