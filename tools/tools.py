import itertools

li = ["a", "b", "c", "d", "e", "f"]

n = itertools.permutations(li, 5)

for x in n:
    print(x)