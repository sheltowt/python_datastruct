

def msort(li):
    if len(li) < 2:
        return li
    result = []
    mid = int(len(li) / 2)
    y = msort(li[:mid])
    z = msort(li[mid:])
    while (len(y) > 0 and len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result



n_sort = [1, 4, 3, 2, 5, 6, 8, 4, 5, 6]
print msort(n_sort)