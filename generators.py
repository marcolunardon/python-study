# GENERATORS
# it's all about save memory!
# Generator functions allow you to declare a function that behaves like an iterator
# generator functions are a special kind of function that return a lazy iterator. 
# These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory
# When you call a generator function or use a generator expression, you return a special iterator called a generator. You can assign this generator to a variable in order to use it. 

# Generator functions look and act just like regular functions, but with one defining characteristic. Generator functions use the Python yield keyword instead of return
# (POINT A)
# yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.
# Instead, the state of the function is remembered. That way, when next() is called on a generator object (either explicitly or implicitly within a for loop), 
# the previously yielded variable num is incremented, and then yielded again.

# (POINT B)
# The performance improvement from the use of generators is the result of the lazy (on demand) generation of values, which translates to lower memory usage.
# Note: Python 2.x only
# This can be illustrated by comparing the range and xrange, Both range and xrange represent a range of numbers, and have the same function signature, 
# but range returns a list while xrange returns a generator
# in Python 3.x, which makes the range built-in return a sequence-type object instead of a list. 

# (POINT C)
# Note: a generator will provide performance benefits only if we do not intend to use that set of generated values more than once. 
# you can iterate through a generator one time only. Once all values have been evaluated, iteration will stop and the loop will exit.

import time
import sys

# THIS: builds the full list in memory -> lot of space occupied for nothing!
def first_n(n):
    '''Build and return a list'''
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

start_time = time.time()
sum_of_first_n = sum(first_n(1000000))
print("First: %s seconds" % (time.time() - start_time))

# Converted to this:
# Generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num   # check (POINT A)
        num += 1

start_time = time.time()
sum_of_first_n = sum(firstn(1000000))
# Memory efficient but way slower!
print("Second: %s seconds" % (time.time() - start_time))



# GENERATOR EXPRESSIONS
# Generator expressions provide an additional shortcut to build generators out of expressions similar to that of list comprehensions.
# In fact, we can turn a list comprehension into a generator expression by replacing the square brackets ("[ ]") with parentheses 
# you’ll have no memory penalty when you use generator expressions.

# list comprehension
nums_squared_lc = [num**2 for num in range(100)]
print("nums_squared_lc is: %s" % (type(nums_squared_lc)))
# generator expression
nums_squared_gc = (num**2 for num in range(100))
print("nums_squared_gc is: %s" % (type(nums_squared_gc)))

# PROFILING Generator expression VS List comprehension
# List comprehension
start_time = time.time()
nums_squared_lc = [num**2 for num in range(100)]
end_time = time.time()
print()
print(" - List comprehension -")
print("Execution: %s seconds" % (end_time - start_time))
print("Memory usage: %s" % (sys.getsizeof(nums_squared_lc)))

# Generator expression
start_time = time.time()
nums_squared_gc = (num**2 for num in range(100))
end_time = time.time()
print()
print(" - Generator expression -")
print("Execution: %s seconds" % (end_time - start_time))
print("Memory usage: %s" % (sys.getsizeof(nums_squared_gc)))

# RESULTS:
# Use List comprehension when memory is not an issue and you want to be fast
# Use Generator expression when memory is an issue and you can be slower


# UNDERSTANDING YIELD:
# Its primary job is to control the flow of a generator function in a way that’s similar to return statements. BUT:
# When the yield statement is hit, the program suspends function execution and returns the yielded value to the caller. 
# (In contrast, return stops function execution completely.) When a function is suspended, the state of that function is saved. 
# This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling.
# This allows you to resume function execution whenever you call one of the generator’s methods. In this way, all function evaluation picks back up right after yield.

# Ex:
def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str

multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))
# Another next() will incurr in an StopIteration exception for exceeding the iterators available
# This is because generators, like all iterators, can be exhausted.
# print(next(multi_obj))


# Advanced Generator Methods:
#   .send()     ->  send values to the generator
#   .throw()    ->  throw exeption from the generator
#   .close()    ->  stop the generator

# to be continued...
