# Find the factorial of a number n using recursion

# Test case:
# In: 5
# Out: 120

# thoughts:
# 5! = 5 * 4 * 3 * 2 * 1

# recursion
# 1) base case
# 2) mutate/change to get closer to base case
# 3) call the function

# in: int
# out: int

# base case: num == 1, return 1

def factorial(num):

	if num == 1:
		return 1

	return num * factorial(num - 1)