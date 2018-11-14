from collections import Counter
scores_list = ['a','b','a','a','b','c']
x_colCount = Counter(scores_list)
type(x_colCount) # <class 'collections.Counter'>
print("  Data: ",scores_list)
print(" + One way to do it:\n")
print("  Value\tCount")
for i in x_colCount:
	print("  ",i,"\t",x_colCount[i])
print("\n + Another way to do it:\n")
for i in x_colCount.most_common():
	print("  ",i)
