# How to sort a Python dict by value
# (== get a representation sorted by value)
d = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

# key=lambda x: x[1] <- styudy better this thing
sort1 = sorted(d.items(), key=lambda x: x[1])
print("Sorted output 1 is :")
print(sort1)

print("\n")

# Or:
import operator
sort2 = sorted(d.items(), key=operator.itemgetter(1))
print("Sorted output 2 is :")
print(sort2)
