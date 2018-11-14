from collections import Counter
scores_list = [7, 8, 9, 2, 10, 9,1,1,0]
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
