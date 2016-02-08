# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class TreeNode():

	def __init__(self,data,left_child,right_child):
		self.key = data
		self.leftChild = left_child
		self.rightChild = right_child

	def hasLeftChild(self):
		return self.leftChild != None

	def hasRightChild(self):
		return self.rightChild != None
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class BinaryTree():

	def __init__(self):
		self.root = None

	def insert(self,data):
		if self.root == None:
			self.root = TreeNode(data,None,None)
		else:
			node,inserted = self.root,False
			while not inserted:
				if data < node.key:
					if node.hasLeftChild():
						node = node.leftChild
					else:
						node.leftChild = TreeNode(data,None,None)
						inserted = True
				else:
					if node.hasRightChild():
						node = node.rightChild
					else:
						node.rightChild = TreeNode(data,None,None)
						inserted = True

	def diameter(self):
		if self.root != None:
			return self.__traverse__(self.root)[2]
		else:
			return 0

	def __traverse__(self,node):
		ll,lr,ld,rl,rr,rd,m_ld,m_rd = [0]*8
		if node.hasLeftChild():
			ll,lr,ld = self.__traverse__(node.leftChild)
			m_ld = max(ll,lr) + 1
		if node.hasRightChild():
			rl,rr,rd = self.__traverse__(node.rightChild)
			m_rd = max(rl,rr) + 1
		# Start Debug.
		# debug_str = "[INFO]    Key: {0}, L-Depth: {1}, R-Depth: {2}, Diameter: {3}"
		# print debug_str.format(node.key, m_ld, m_rd, max(ld, m_ld + m_rd, rd))
		# End Debug.
		return m_ld, m_rd, max(ld, m_ld + m_rd, rd)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def __test__():
	# Building Sample Tree:
	T = BinaryTree()
	keys = [15,2,1,0,8,7,5,4,3,6,13,9,11,10,12,14,16,18,17,19]
	for data in keys:
		T.insert(data)
	print "Diameter of Tree: {0}".format(T.diameter())
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
__test__()
