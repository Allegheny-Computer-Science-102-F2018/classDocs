def calculate_mean(numbers_list):
  print("  Values", numbers_list)
  s_int = sum(numbers_list)
  N_int = len(numbers_list)
  # Calculate the mean
  mean_flt = s_int/N_int
  return mean_flt
#end of calculate_mean()
if __name__ == '__main__':
    donations_list = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean_flt = calculate_mean(donations_list)
    N_int = len(donations_list)
    print('  The mean of the {0} values is {1}'.format(N_int, mean_flt))
