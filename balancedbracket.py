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