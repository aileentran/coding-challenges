"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""

# soo.. it takes in two strings
# returns boolean: true - 0 or 1 letters off; false otherwise 

#maybe have a counter
#two for loops simultaneously? 
#or one loop with checking in second word 

#if counter < 1, return false, else true 

#ohh!! order of letters DO matter
#so.. two unnested loops?

# woaaah.. using a while loop => access indexes of both strings 
# okay.. so first faily quickly if the length differences is >1 (2 or more)

#check length of both words
#pick the shortest string out of the words to loop through 

#create a mismatch counter

#make the while loop: i and k (bc i visually get tripped up btwn i and j lol!)
#so if the letter's DONT match, counter ++
# increment longer word
# if the words are both the same length, increment the "shorter" word too!
# otherwise, both letters are the same and we increment both
def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    longer = w1
    shorter = w2

    if len(shorter) > len(longer):
        longer = w2
        shorter = w1

    if len(longer) - len(shorter) > 1:
        return False 

    mismatch = 0

    # while loopin~
    # i idx of longer word
    # k idx of shorter word

    i = k = 0
    # setting loop based on shorter word :o 
    while k < len(shorter):
        if shorter[k] != longer[i]:
            mismatch += 1

            if mismatch > 1:
                return False

            i += 1

            # if both words are of the same length
            if len(longer) == len(shorter):
                k += 1

        # letter matches!
        else:
            i += 1
            k += 1

    # mismatch <= 1
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
