"""
Write a function that accepts:

garden
A list of the garden cells with carrot counts. This will be a list of rows, with each row being a list of columns.

This function should return the number of carrots eaten.

Note: WNES -> direction order = check left, up, right, down 

Test cases:
>>> garden = [
...     [1, 1, 1],
...     [0, 1, 1],
...     [9, 1, 9]
... ]

>>> lunch_count(garden)
3

This starts at 4 (highest of the four middle), then goes right:

>>> garden = [
...     [9, 9, 9, 9],
...     [9, 3, 1, 0],
...     [9, 1, 4, 2],
...     [9, 9, 1, 0],
... ]

>>> lunch_count(garden)
6

>>> garden = [
...     [2, 3, 1, 4, 2, 2, 3],
...     [2, 3, 0, 4, 0, 3, 0],
...     [1, 7, 0, 2, 1, 2, 3],
...     [9, 3, 0, 4, 2, 0, 3],
... ]

>>> lunch_count(garden)
15

"""

# thoughts

# row = garden[#]
# col = garden[#][#]
# garden[row][col]

# WNES
# west = left = garden[row][col-1]
# north = up = garden[row-1][col]
# east = right = garden[row][col+1]
# south = down = garden[row+1][col]

# variable most carrots = 0; NOTE: need to reset each time after entering cell!
# start = []

# to start
# need to access middle of the matrix: middle row, middle columns
# if even number, get two middle rows and/or two middle columns
# INDEXES = want to round.. down..?

# >>> garden = [
# ... [1, 1, 1],
# ... [0, 1, 1],
# ... [9, 1, 9]
# ... ]
# >>> garden[1][1]
# 1

# >>> garden[start[0][0]][start[0][1]]
# 1

import math

# helper function - WHERE DO I BEGINN?
def start(garden, nrows, ncols):
	"""Figuring out where to start."""

	start_coords = []

	# even rows and columns
	row1 = math.floor(nrows/2)
	row2 = row1 - 1
	col1 = math.floor(ncols/2)
	col2 = col1 - 1

	# odd rows and columns
	row_odd = math.floor(nrows/2)
	col_odd = math.floor(ncols/2)

	if nrows % 2 != 0 and ncols % 2 != 0:
		start_coords.append([row_odd,col_odd])
	elif nrows % 2 == 0 and ncols % 2 != 0:
		start_coords.append([row1, col_odd])
		start_coords.append([row2, col_odd])
	elif nrows % 2 != 0 and ncols % 2 == 0:
		start_coords.append([row_odd, col1])
		start_coords.append([row_odd, col2])
	elif nrows % 2 == 0 and ncols % 2 == 0:
		start_coords.append([row1, col1])
		start_coords.append([row1, col2])
		start_coords.append([row2, col1])
		start_coords.append([row2, col2])

	return start_coords		



def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    start(garden, nrows, ncols)



