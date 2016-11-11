def quicksort(li):
    less = []
    greater = []
    equal = []

    if len(li) > 1:
        pivot = li[0]
        for x in li:
            if x > pivot:
                greater.append(x)
            if x == pivot:
                equal.append(x)
            if x < pivot:
                less.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return li



#breaks into ten buckets, and then runs quicksort on each bucket
def bucket_sort(seq):
    biggest = 0
    for number in seq:
        if number > biggest:
            biggest = number
    buckets_num = int(biggest / 10 + 1)
    buckets = []
    for i in range(buckets_num):
        buckets.append([])
    for number in seq:
        chunk = number / 10
        buckets[chunk].append(number)
    for index, bucket in enumerate(buckets):
        #Using quicksort to sort individual buckets
        buckets[index] = quicksort(bucket)
    new_list = []
    for bucket in buckets:
        new_list += bucket
    return new_list

print bucket_sort([1, 2, 3, 4, 5, 76, 3, 56, 4, 98, 3])