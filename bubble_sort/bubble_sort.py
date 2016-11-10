# O(N^2)

def bubbleSort(li):
	for passnum in range(len(li)-1, 0, -1):
		for x in range(passnum):
			if li[x] > li[x+1]:
				temp = li[x]
				li[x] = li[x+1]
				li[x+1] = temp
	return li


alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print alist
