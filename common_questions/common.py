#FizzBuzz

def FizzBuzz(n):
	if n % 3 == 0 and n % 5 == 0:
		return "FizzBuzz"
	if n % 3 == 0:
		return "Fizz"
	if n % 5 == 0:
		return "Buzz"
	else:
		return str(n)

print "\n".join(fizzbuzz(n) for n in xrange(1, 21))




#Fibonacci





#MergeSort




#Priority Heap




#Tree Questions