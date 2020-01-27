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