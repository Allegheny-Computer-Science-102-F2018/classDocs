''' Find the variance and standard deviation of a list of numbers'''
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    # Calculate the mean
    mean = s/N
    return mean
#end of calculate_mean()

def find_differences(numbers_list):
    # Find the mean
    mean = calculate_mean(numbers_list)
    # Find the differences from the mean
    diff_list = []
    for num in numbers_list:
       diff_list.append(num-mean)
    return diff_list
#end of find_differences()

def calculate_variance(numbers):
       # Find the list of differences
       diff_list = find_differences(numbers)
       # Find the squared differences
       squared_diff_list = []
       for d in diff_list:
           squared_diff_list.append(d**2)
       # Find the variance
       sum_squared_diff_list = sum(squared_diff_list)
       # better estimate for large populations
       variance = sum_squared_diff_list/(len(numbers)-1)
       return variance
#end of calculate_variance()

if __name__ == '__main__':
       donations_list = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
       variance = calculate_variance(donations_list)
       print("  Data:",donations_list)
       print('The variance of the list of numbers is {0}'.format(variance))
       std = variance**0.5 # sqrt of variance
       print('The standard deviation of the list of numbers is {0}'.format(std))
