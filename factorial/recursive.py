def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n -1)
print factorial(10)


def iterative_factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
        print num
    return num

print iterative_factorial(100)