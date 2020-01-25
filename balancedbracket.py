"""Given a string, return True or False depending on whether the string’s opening-and-closing marks (that is, brackets) are balanced. Account for the following bracket types: (), [], {}, <>

Test cases:
>>> has_balanced_brackets("<ok>")
True

>>> has_balanced_brackets("<[ok]>")
True

>>> has_balanced_brackets("<[{(yay)}]>")
True

These are invalid, as they close brackets that weren’t open:
>>> has_balanced_brackets(">")
False

>>> has_balanced_brackets("(This has {too many} ) closers. )")
False

wrong order:

>>> has_balanced_brackets("<{Not Ok>}")
False

no brackets, consider it balanced:

>>> has_balanced_brackets("No brackets here!")
True
"""

# thoughts
# input: string - chars and brackets 
# output: boolean, true - no brackets or balanced; false - unbalanced, wrong order

# order of closers more important - dictionary to keep track of them? 
# key: closer, value: opener 

# make function
# dictionary for closers (key) and openers (value)
# openers for empty list

# loop through string - for loop!
# umm.. put the openers in list. 
# when encounter a closer - check if value matches last opener in list
# if so, pop it off
# if not, return false

# outside loop 
# return true

def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    closers = {
    	")" : "(",
    	"}" : "{",
    	"]" : " [",
    	">" : "<"
    }

    brackets = []

    for char in phrase:
    	if char == "(" or char == "[" or char == "{" or char == "<":
    		brackets.append(char)
    	if char in closers:
    		if closers[char] != brackets[-1]:
    			return False
    		else:
    			brackets.pop()

    return True