"""
The “mode” of a list is the set of item(s) that occur the most often. For example, in [1, 2, 2, 3], 2 is the most commonly-occurring item.

Where there is a tie, the mode is all items that are tied for most common: in [1, 1, 2, 2, 3], the mode is both 1 and 2.

In this challenge, you should write a function that returns the mode.

It should always return a set, even if there’s only one item in the set

Test case:
>>> mode([1]) == {1}
True

>>> mode([1, 2, 2, 2]) == {2}
True

If there is a tie, return all:

>>> mode([1, 1, 2, 2]) == {1, 2}
True

"""

# thoughts
# input: list of nums
# output: set - most occuring num(s)

# create empty set variable to return 
# have a counter of sorts - dictionary? 

# loop through list and count in dictionary
# loop through dictionary and.. if value is == current value, append the num to set 
# if value is greater than the ones in the set, set = current num...? 

def mode(nums):
	"""Find mode of the all the nums in list."""
	# dictionary
	counter ={}
	# set
	result = {}

	for num in nums:
		if num not in counter:
			counter[num] = 1
		else:
			counter[num] += 1

	return counter