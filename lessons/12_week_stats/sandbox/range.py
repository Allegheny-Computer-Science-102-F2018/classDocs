''' Find the range '''
def find_range(numbers_list):
  print("  Values: ",numbers_list)
  lowest_int = min(numbers_list)
  highest_int = max(numbers_list)
  # Find the range
  r_int = highest_int - lowest_int # find distance
  return lowest_int, highest_int, r_int
#end of find_range()

if __name__ == '__main__':
  donations_list = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
  lowest, highest, r = find_range(donations_list)
print('  Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))
