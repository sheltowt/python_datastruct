
def msort(n):
	if len(n) < 2:
		return n
	result = []
	mid = int(len(n) / 2)
	y = msort(n[:mid])
	z = msort(n[mid:])
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