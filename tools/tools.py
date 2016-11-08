import itertools

li = ["a", "b", "c", "d", "e", "f"]

n = itertools.permutations(li, 5)

for x in n:
    print(x)


# range versus xrange, range is faster but takes up significantly less memory

