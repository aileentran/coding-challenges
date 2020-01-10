# input: list of nums
# output: boolean - True if contains ANY nums that add to 0 OR if 0, False otherwise

# only integers in list 

# test cases
# [0] = True
# [1, -1] = True
# [7, 8, -10] = False

# thoughts
# create a function that takes in a list of numbers
# return True fast - if 0 even in the list, return true! 

# loop through list of nums
# if the list has negative version of the number, return true

# outside of loop, return false 

def add_to_zero(nums):
	"""Check if any of the numbers sum to zero (or is zero)."""
	if 0 in nums:
		return True

	for num in nums:
		if -num in nums:
			return True

	return False