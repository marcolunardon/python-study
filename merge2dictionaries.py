# Merging 2 dictionaries

# Dictionary definition - TYPE 1
dict1 = {}
dict1["a"] = 1
dict1["b"] = 2

# Dictionary definition - TYPE 2
dict2 = { 
    "c": 4,
    "b": 3
}


# Python3
merged = {**dict1, **dict2}

# Python2
#merged = dict(dict1, **dict2)

print(merged)

