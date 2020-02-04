"""Determine if the given word is a re-scrambling of a palindrome.

The word will only contain lowercase letters, a-z.

Doesn't need to be a real word

Test cases:
>>> is_anagram_of_palindrome("a")
True

>>> is_anagram_of_palindrome("ab")
False

>>> is_anagram_of_palindrome("aab")
True

>>> is_anagram_of_palindrome("arceace")
True

>>> is_anagram_of_palindrome("arceaceb")
False

"""

# thoughts
# input: string
# output: boolean - true if anagram of palindrome, false otherwise 
# can return true early if one letter 
# have a counter -> dictionary? 

# palindrome, 1 or less letter can have an odd number
# everything else needs to be even.. 
# if there are more than one letter that has an odd number, return false

def is_anagram_of_palindrome(anagram):
	"""Check if string is an anagram of palindrome."""
	if len(anagram) == 0:
		return True

	counter = {}

	for letter in anagram:
		if letter not in counter:
			counter[letter] = 1
		else:
			counter[letter] += 1

	odd = 0
	for letter in counter:
		if counter[letter] % 2 != 0:
			odd += 1

	if odd <= 1:
		return True

	return False


