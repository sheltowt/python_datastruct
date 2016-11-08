# python_datastruct

https://www.interviewcake.com/article/java/big-o-notation-time-and-space-complexity

http://stackoverflow.com/questions/2307283/what-does-olog-n-mean-exactly

https://github.com/johnshiver/algorithms

http://www.developer.com/mgmt/three-types-of-interview-questions-software-developers-should-expect.html

Timing

O(1) - constant time, just one step
describes an algorithm that will always execute in the same amount of time

return True


O(n) - linear time, as it grows, add one more item
describes an algorithm whose performance will grow linearly with time, and in direct proportion to the size of the input data set

for element in str:
	print element


O(n^2) - quadratic time, two for loops
algorithm whose performance is directly proportional to the square of the size of the input data set

for element in str:
	for element2 in str:
		element3 = element + element2


n could be the actual input or size of input

O(2n) is actually O(n)
denotes exponential growth -> starts small and then grows exponentially

def Fibonacci(number):
	if number <= 1:
		return number

	return Fibonacci(number -2) + Fibonacci(number -2)

log n -> logarithmic, binary search, pick random point in book, pick next closest half

n log n -> log linear

O(n + n^2) is actually O(n^2) -> take most specific


