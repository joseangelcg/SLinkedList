import sys

class Node:
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.next = None

	def setNext(self, node):
		self.next = node

	def setValue(self, val):
		if (self != None):
			self.val = val

	def __repr__(self):
		return str(self.val)

class SLinkedList:
	"""docstring fos SLinkedList"""

	def __init__(self, node=None):
		self._head = node
		self._size = 1 if (node != None) else 0

	def __len__(self):
		return self._size

	def addNode(self, node):
		a = self._head
		
		if(a == None):
			self._head = node
		else:
			while(a.next != None):
				a= a.next

			a.setNext(node)
		
		self._size += 1

	def containsVal(self, val):
		"""
			Searches for a specific value in the current List

			Return value:
				True if val exists in SlinkedList instance
				False otherwise
		"""
		if (self._head != None):

			a = self._head
			while(a != None):
				if(a.val == val):
					return True
				a = a.next

		return False

	def removeVal(self, val):
		"""
			Removes val in the current List
			If val is not in the list, nothing happens

			Return value:
				None
		"""
		if(self._head != None):

			if(self.containsVal(val)):

				if(self._size == 1):
					del(self._head)
					self._head = None
				else:
					a = self._head
					b = None

					if(a.val == val):
						self._head = a.next
						del(a)
					else:
						while(a.val != val):
							b = a
							a = a.next

						b.setNext(a.next)
						del(a)

				self._size -= 1

	def addVal(self, val):
		a = self._head
		temp = Node(val)

		if(a == None):
			self._head = temp
		else:
			while(a.next != None):
				a= a.next

			a.setNext(temp)
		
		self._size += 1

	def get(self, index):
		if(index < len(self)):
			if(index):
				a=self._head
				for i in range(0,index):
					a = a.next
				return a.val
			else:
				return self._head.val
		return None

	def __repr__(self):
		a = self._head
		str1 = str(a.val)

		while(a.next != None):
			a = a.next
			str1 += " -> " + str(a.val)

		return str1 


#Test code

List1 = SLinkedList()
List1.addVal(5)
List1.addVal(7)
List1.addVal(8)
print(List1)
print(len(List1))

List1.removeVal(5)
print(List1)
print(List1.get(2))

