
# zip together lists containing 20 elements each, each element is three-tuple



def maxSequence(arr):
	# ... 
    max = 0
    for i in range(len(arr)):
        subs = zip(*(arr[z:] for z in range(i)))
        for x in subs:
            num = sum(x)
            if num > max:
                max = num
    return max