"""
We want a function that will delete a node from the series, so that everything moves over by one.

Given a node in a linked list, remove it.

Remove this node from a linked list. Note that we do not have access to
any other nodes of the linked list, like the head or the tail.

Does not return anything; changes list in place.
"""

# thoughts
# need to make Node class
# have access to node.data and node.next
# input: node to remove
# output: nothing...? so we print the list?

# general idea.. 
# current node.data = node.next.data
# current node.next = None
# then print the thingy?

class Node(object):
	"""Class in a linked list."""

	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def as_string(self):
		"""Representing data for this node and successors as a string.
		>>> Node(3).as_string()
		'3'

		>>> Node(3, Node(2, Node(1))).as_string()
		'321'

		"""

		out = []
		n = self

		while n:
			out.append(str(n.data))
			n = n.next

		return "".join(out)


def remove_node(node):
	"""Remove current node."""

	if not node.next:
		raise ValueError('Cannot remove tail node.')

	node.data = node.next.data
	node.next = node.next.next
