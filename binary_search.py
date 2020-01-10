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
# make a counter = 1
# make lower and upper range variables?
# the_range = range(0, 101)

# loop 
# guess = the_range / 2
# lower = range(0, guess)
# upper = range(guess, val)

# returning true early!! 
# if guess == num, return counter

# while guess != num
# num > guess
# counter += 1
# the_range = range(guess, 101)
# guess = the_range / 2
# lower = 