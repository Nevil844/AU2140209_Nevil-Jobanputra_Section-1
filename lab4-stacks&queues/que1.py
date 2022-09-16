
from inspect import stack


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.head = None

	def isempty(self):
		if self.head == None:
			return True
		else:
			return False

	def push(self, data):

		if self.head == None:
			self.head = Node(data)

		else:
			newnode = Node(data)
			newnode.next = self.head
			self.head = newnode

	def pop(self):

		if self.isempty():
			return None

		else:

			poppednode = self.head
			self.head = self.head.next
			poppednode.next = None
			return poppednode.data


	def display(self):

		iternode = self.head
		if self.isempty():
			print("Stack Underflow")

		else:

			while(iternode != None):

				print(iternode.data, "->", end=" ")
				iternode = iternode.next
			return


myStack = Stack()

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)

myStack.display()

print("  ")


myStack.pop()
myStack.pop()


myStack.display()


