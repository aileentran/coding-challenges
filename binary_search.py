"""
To do this, you examine the middle item and, if the sought-for value is smaller, move halfway to the left. If the sought-after value is larger, move halfway to the right.

In this challenge, you’ll make binary search for the classic children’s guessing game of “pick a number from 1 to 100”.

Since you use binary search, it will never take more than 7 guesses for a function to find a number in the range 1 to 100 (since log2 100) is just a little under 7).

Test cases:
>>> binary_search(50)
1

>>> binary_search(25)
2

>>> binary_search(75)
2

>>> binary_search(31) <= 7
True

>>> max([binary_search(i) for i in range(1, 101)])
7
"""

# thoughts
# input: number to look for
# output: int - number of guesses made - needs to be 7 or less

# make a function that takes in a number 
# make low and upper - ints, not ranges!!
# lower = 0
# higher = 101
# num_of_guess = 0
# guess = None

# while loop : guess not = num
# num_of_guess += 1
# guess = higher // 2

# if num > guess
# lower = guess

# else: if num < guess
# higher = guess

# outside loop - return num of guesses

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    lower = 0
    upper = 101
    guess = None

    while guess != val:
    	num_guesses += 1
    	guess = (lower - upper) // 2
    	print("guess", guess)
    	print("lower", lower)
    	print("upper", upper)

    	if val > guess:
    		lower = guess
    	elif val < guess:
    		upper = guess

    return num_guesses




