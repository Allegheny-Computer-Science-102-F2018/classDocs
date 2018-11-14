''' Calculating the median '''
def calculate_median(numbers_list):
#    print(" calculate_mean()")
    N = len(numbers_list)
    numbers_list.sort()
    # Find the median
    if N % 2 == 0:
        # if N is even
        m1 = N/2
        m2 = (N/2) + 1
        # Convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median_int = (numbers_list[m1] + numbers_list[m2])/2
    else:
        m = (N+1)/2
        # Convert to integer, match position
        m = int(m) - 1
        median_int = numbers_list[m]
    return median_int

if __name__ == '__main__':
       donations_list = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
       print("  Data:",donations_list)
       median_int = calculate_median(donations_list)
       N = len(donations_list)
       print('  Median donation over the last {0} days is {1}'.format(len(donations_list), median_int))
