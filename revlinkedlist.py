"""Write a function that takes the head node of a linked list and returns the head of a new linked list, where the nodes are in the reverse order.

Test case:
>>> ll = Node(1, Node(2, Node(3)))
>>> new_ll = reverse_linked_list(ll)
>>> new_ll.as_string()
'321

"""

# thoughts
# input: head of linked list
# output: head of linked list (reversed)

# create node class w/being able to print linked list as a string
# self.data, self.next 
# while loopin and etc. 

# function takes in linked list
# make an.. empty node? or set the node to the first value in linked list 

# traverse through linked list 
# set each node as the head (clean slate)
# once we hit node.next == None --> break loop

# we return the head of the list

class Node(object):
	"""Create node."""

	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def as_string(self):
		"""Print node and all it's successors as a string."""

		out = []
		n = self

		while n:
			out.append(str(n.data))
			n = n.next

		return "".join(out)


def rev_ll(node):
	head = None

	while node:
		# create a new head node!
		head = Node(node.data, head)
		node = node.next

	return head
