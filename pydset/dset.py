# Disjoint Set Data Structure for Python 2.
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

class DisjointSet():

	"""
	Disjoint Set Data Structure.
	Format: Data is stored in a HashMap of Key-Value Pairs
			with keys being the object and values being the
			parent of the object.
	Example: ['A':'A','B':'A','C':'B','D':'D','E':'D'] would
			 have the following structure:
			 	A 		D
			   /   	   /
			  B 	  E
			 /
		    C
	"""

	def __init__(self):
		self.data = {}
		self.roots = set()

	def add(self,root):
		if root.__class__.__name__ == 'list':
			for key in root: self.data[key] = key
		else: self.data[root] = root
		self.roots = self.roots.union(root)

	def union(self,keyOne,keyTwo):
		rootOne,depthOne = self.find(keyOne)
		rootTwo,depthTwo = self.find(keyTwo)
		if depthOne > depthTwo: 
			self.data[rootTwo] = rootOne
			self.roots.remove(rootTwo)
		else: 
			self.data[rootOne] = rootTwo
			self.roots.remove(rootOne)

	def find(self,key):
		if key not in self.data:
			raise Exception('Key Not Found!')
		else:
			parent,depth = key,0
			while parent != self.data[parent]:
				parent = self.data[parent]
				depth += 1
			return (parent,depth)

	def compress(self):
		for key in self.data.keys():
			self.data[key] = self.find(key)[0]

	def numTrees(self):
		return len(self.roots)

	def __repr__(self):
		info = 'Disjoint Set Adjacency List:\n'
		hashMap = {}
		for k,v in self.data.items():
			if v not in hashMap: hashMap[v] = []
			if k != v: hashMap[v].append(k)
		return info+'\n'.join([str(k)+': '+','.join([str(x) for x in v]) for k,v in hashMap.items()])
