# this is a great merge sort

def msort2(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x)/2)
    y = msort2(x[:mid])
    z = msort2(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    print result



def msort(x):
    if len(x) < 2:
        return x
    result = []          # moved!
    mid = int(len(x)/2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    print result
    return result

n_sort = [1, 4, 3, 2, 5, 6, 8, 4, 5, 6]
print msort(n_sort)