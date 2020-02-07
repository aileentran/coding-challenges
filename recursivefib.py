# recursive function that takes in n and returns nth Fib number
# Fib: 1, 1, 2, 3, 5, 8, 13, 21, etc. 

# test cases
# fib(1) = 1
# fib(2) = 1
# fib(3) = 2

# thoughts
# in: int (NOT index)
# out: fib number at that position

# recursion:
# 1) base case
# 2) change to get closer to base case
# 3) call same function

# base case:
# n = 1 or 2, return 1

# change:
# (n - 1) + (n - 2)

def fib(n):
	"""Return nth Fibonacci number."""

	if n <= 2:
		return 1

	return fib(n - 1) + fib(n - 2)