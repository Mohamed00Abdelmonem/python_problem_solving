def invert(lst):
    #  usign list comprehantion
    return [-n for n in lst]

print(invert([1, 2, 3, 4, 5]))
print(invert([1, -2, -3, -4, -5]))
print(invert([]))
