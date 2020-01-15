"""
A valid code is a sequence of numbers and letters, always starting with a number and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter. After each good letter should come the next next number.

For example, the string “hey” could be encoded by “0h1ae2bcy”. This means “skip 0, find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.

Test cases:
>>> decode("0h")
'h'

>>> decode("2abh")
'h'

>>> decode("0h1ae2bcy")
'hey'
"""

# thoughts
# input: string - #abc blah
# output: string - abc

# num = letters to skip
# 0 = don't skip
# 1 = skip one letter and get 2nd following num
# 2 = skip two letters and get 3rd
# maaybe.. get the num + current index + 1? 
# + 1 to.. skip over idx of current number..??? 

# make function
# make empty string to concatenate result into 

# loop through string - maaybeeeeee... enumerate?
# if char is an int 
# num + (next char = current idx + 1)
# append value into string 

# return string

def decode(string):
	"""Decode a string."""

	decoded = ""


	for idx, char in enumerate(string):
		if isinstance(char, int) == True:
			code_idx = char + idx + 1
			print("idx", idx)
			print("code_idx", code_idx)
			decoded += string[code_idx]
			print(string[code_idx])

	return decoded

