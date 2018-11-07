# date: 7 Nov 2018
# simple plotting tool for frequencies of characters in a string

from pylab import plot, show, title, savefig, xlabel, ylabel, legend

s_str = "hello" # string to study
sCount_dict = {} # save the counts here

# count the letters in the word
for i in s_str:
    if i not in sCount_dict:
        sCount_dict[i] = 1 # add the char to the dictionary with count of one
    else: # this char is already in the dictionary
        sCount_dict[i] = sCount_dict[i] + 1

print("sCount_dict:",sCount_dict)

# store freqs

freq_list = [] # list of the frquencies for the chars
for i in sCount_dict:
    freq_list.append(sCount_dict[i]/len(s_str))

print(" freq_list :",freq_list)

y = freq_list
x = [i for i in range(len(freq_list))]
plot(x,y, marker = 'o')
show()
