# Different ways to test multiple flags at once
# Same line initialization of different values (different from C++)
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed 1st')

if 1 in (x, y, z):
    print('passed 2nd')

# These only test for truthiness:
if x or y or z:
    print('passed 3rd')

# this is funny!
if any((x, y, z)):
    print('passed 4th')