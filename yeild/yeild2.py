# generators are iterators but you can only iterate over them once
# function will return a generator


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i