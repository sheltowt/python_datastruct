#quicksort

def quicksort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        print(array)
        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

li = [5, 43, 2, 5, 7, 8, 5, 3, 89, 65]
print quicksort(li)

#breaks into ten buckets, and then runs quicksort on each bucket
def bucket_sort(seq):
    biggest = 0
    for number in seq:
        if number > biggest:
            biggest = number
    buckets = []
    buckets.append([]) * (biggest / 10 + 1)
    for number in seq:
        buckets[number / 10].append(number)
    for index, bucket in enumerate(buckets):
        #Using quicksort to sort individual buckets
        buckets[index] = quicksort(bucket)
    new_list = [number for number in bucket for bucket in buckets]
    return new_list