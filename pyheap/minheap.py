# Copyright (c) 2016 Pragaash Ponnusamy.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class MinHeap():

	"""
	Array-based Heap that satisfies a Minimum Value Heap
	Order Property. This implementation supports key-value
	pairs of objects as nodes of the heap.
	Example: 	
			('A',1)
			  / \
		('B',3)  ('C',5)
	"""

	def __init__(self):
		self.heap = []
		self.data = {}
		self.size = 0


	def isEmpty(self):

		return self.size == 0


	def push(self,key,value):
		L = self.size
		self.data[key] = [[value],L]
		self.heap.append((key,self.data[key][0]))
		self.size += 1
		ordered = False
		N,parent = L,None
		while not ordered:
			parent = (N-1)//2
			if parent >= 0 and value < self.heap[parent][1][0]:
				self.swapInHeap(N,parent)
				N = parent
			else: ordered = True


	def pop(self):
		if self.size > 0: return self.__removeMin__()
		else: raise Exception('Heap is Empty!')		


	def __removeMin__(self):
		self.swapInHeap(0,self.size-1)
		key,value = self.heap.pop()
		self.data.__delitem__(key)
		self.size -= 1
		if self.size > 0:
			ordered,N = False,0
			while not ordered:
				childOne,childTwo,mKey = 2*N+1,2*N+2,self.heap[N][1]
				if childOne == self.size-1 and mKey > self.heap[childOne][1]:
					self.swapInHeap(N,childOne)
					N = childOne
				elif childTwo < self.size and (mKey > self.heap[childOne][1] or mKey > self.heap[childTwo][1]):
					K = min(childOne,childTwo,key=lambda x: self.heap[x][1])
					self.swapInHeap(N,K)
					N = K
				else: ordered = True
		return (key,value[0])


	def find(self,key):
		if key in self.data: return self.data[key][0][0]
		else: raise Exception('Key not in Heap!')


	def peek(self):
		if self.size > 0: return zip(*self.heap[0])[0]
		else: raise Exception('Heap is Empty!')


	def heapify(self):

		if self.size > 1: self.__makeheap__()


	def __makeheap__(self):
		L,K,modified = self.size,0,False
		childOne,childTwo,grandParent,parent = [None]*4
		while K < L:
			if not modified:
				childOne,childTwo,grandParent = 2*K+1,2*K+2,(K-1)//2
				parent = self.heap[K][1]
				modified = True
			else: 
				if (childOne < L) and (parent > self.heap[childOne][1]):
					self.swapInHeap(parent,childOne)
				elif (childTwo < L) and (parent > self.heap[childTwo][1]):
					self.swapInHeap(parent,childTwo)
				elif (grandParent >= 0) and (parent < self.heap[grandParent][1]):
					self.swapInHeap(parent,grandParent)
				else:
					modified = False
					K += 1


	def emptyHeap(self):
	
		self.__init__()


	def update(self,key,value):
		if key in self.data:
			self.data[key][0][0],L = value,self.size
			ordered,parent,N = False,None,self.data[key][1]
			while not ordered:
				parent,childOne,childTwo = (N-1)//2,2*N+1,2*N+2
				if (parent >= 0) and ([value] < self.heap[parent][1]):
					self.swapInHeap(N,parent)
					N = parent
				elif childOne == L-1 and [value] > self.heap[childOne][1]:
					self.swapInHeap(N,childOne)
					N = childOne
				elif childTwo < L and ([value] > self.heap[childOne][1] or [value] > self.heap[childTwo][1]):
					K = min(childOne,childTwo,key=lambda x: self.heap[x][1])
					self.swapInHeap(N,K)
					N = K
				else: ordered = True
		else: raise Exception('Key not in Heap!')


	def swapInHeap(self,a,b):
		self.data[self.heap[a][0]][1] = b
		self.data[self.heap[b][0]][1] = a
		tmp = self.heap[a]
		self.heap[a] = self.heap[b]
		self.heap[b] = tmp


	def __repr__(self):
		
		return str(map(lambda (k,v): (k,v[0]),self.heap))




