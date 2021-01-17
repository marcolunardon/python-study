# Packing and unpacking arguments:

# Packing argument happens when you call a function with a list of arguments treated as a single variable. Using a Tuple as an example.
# Packing is used When we don’t know how many arguments need to be passed to a python function.

# Unpacking arguments happens when you call a function with a single variable structure that contains multiple element and the function will unpack them. Using a list as an example.
# Upacking is used: We can use * to unpack the list so that all elements of it can be passed as different parameters.


list1 = [1,2,3,4]       #list
tuple1 = (1, 2, 3, 4)   #tuple
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd' : 4}   #dictionary


####################
# PACKING ARGUMENTS:
####################

# sum all input numbers
# unknown number of arguments in input
def functPacking(*args):
    sum = 0
    #myList = list(args)   # optional
    for n in range(0, len(args)):
        sum = sum + args[n]
    return sum


# # Packing using lists
# print("Packing with lists")
# functPacking(list1)

# Packing using tuples
print("Packing with tuples")
print(functPacking(1,2, 3, 4,))

# # Packing using dictionaries
# print("Packing with dictionaries")
# functPacking(dict1)


######################
# UNPACKING ARGUMENTS:
######################

def functUnpacking(a,b,c,d):
    print(a,b,c,d)


# Unpacking using lists
print("Unpacking with lists")
functUnpacking(*list1)

# Unpacking using tuples
print("Unpacking with tuples")
functUnpacking(*tuple1)

# Unpacking using dictionaries
print("Unpacking with dictionaries")
functUnpacking(**dict1)