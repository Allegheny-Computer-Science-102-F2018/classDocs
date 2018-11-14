'''Frequency table for a list of numbers'''
from collections import Counter
def frequency_table(numbers_list):
    print("  numbers_list:", numbers_list,"\n")
    table = Counter(numbers_list)
    print('  Number\tFrequency')
    for number in table.most_common():# count occurrences
    # go through each of the tuples, printing the first member (the value itself) and the second value which is its  frequency of occurrence
        print('  {0}\t{1}'.format(number[0], number[1]))

if __name__=='__main__':
 scores_list = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
 frequency_table(scores_list)
