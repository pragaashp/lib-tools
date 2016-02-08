import unittest
from minheap import MinHeap

class MinHeapTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.H = MinHeap()
		self.data = [('A',7),('B',3),('C',4),('D',1),('E',6),('F',5),('G',2)]

	@classmethod
	def tearDownClass(self):
		self.H = None

	def check_assertions(self,heap_val,data_val,size_val):
		self.assertEqual(self.H.heap,heap_val,'Non-Empty Heap')
		self.assertEqual(self.H.data,data_val,'Non-Empty Data')
		self.assertEqual(self.H.size,size_val,'Non-Zero Size')

	def test_empty_heap_1_func(self):
		self.H.emptyHeap()
		self.check_assertions([],{},0)

	def test_empty_heap_2_pop(self):
		self.assertRaises(Exception,self.H.pop)

	def test_empty_heap_3_find(self):
		self.assertRaises(Exception,self.H.find,'A')

	def test_empty_heap_4_peek(self):
		self.assertRaises(Exception,self.H.peek)

	def test_empty_heap_5_heapify(self):
		self.H.heapify()
		self.check_assertions([],{},0)

	def test_empty_heap_6_update(self):
		self.assertRaises(Exception,self.H.update,'A',3)

	def test_single_entry_heap_1_push(self):
		self.H.emptyHeap()
		self.H.push('A',3)
		self.check_assertions([('A',[3])],{'A':[[3],0]},1)

	def test_single_entry_heap_2_find(self):
		self.assertEqual(self.H.find('A'),3)
		self.assertRaises(Exception,self.H.find,'B')

	def test_single_entry_heap_3_peek(self):
		self.assertEqual(self.H.peek(),('A',3))

	def test_single_entry_heap_4_heapify(self):
		self.H.heapify()
		self.check_assertions([('A',[3])],{'A':[[3],0]},1)

	def test_single_entry_heap_5_update(self):
		self.H.update('A',7)
		self.check_assertions([('A',[7])],{'A':[[7],0]},1)

	def test_single_entry_heap_6_pop(self):
		self.assertEqual(self.H.pop(),('A',7))
		self.check_assertions([],{},0)

	def check_heap_order_property(self):
		N = self.H.size
		for k in range(N):
			x,y = self.H.heap[k]
			self.assertEqual(self.H.data[x],[y,k])
			childOne,childTwo,parent = 2*k+1,2*k+2,(k-1)//2
			if parent >= 0: 
				p = self.H.heap[parent]
				self.assertGreater(y,p[1])
				self.assertEqual(self.H.data[p[0]],[p[1],parent])
			if childOne < N:
				c = self.H.heap[childOne]
				self.assertLess(y,c[1])
				self.assertEqual(self.H.data[c[0]],[c[1],childOne])
			if childTwo < N:
				c = self.H.heap[childTwo]
				self.assertLess(y,c[1])
				self.assertEqual(self.H.data[c[0]],[c[1],childTwo])


	def test_multiple_entry_heap_1_push(self):
		self.H.emptyHeap()
		for k,v in self.data:
			self.H.push(k,v)
			self.check_heap_order_property()

	def test_multiple_entry_heap_2_peek(self):
		self.assertEqual(self.H.peek(),('D',1))

	def test_multiple_entry_heap_3_find(self):
		for k,v in self.data:
			self.assertEqual(self.H.find(k),v)

	def test_multiple_entry_heap_4_heapify(self):
		values = self.H.data.values()
		self.H.heapify()
		self.assertEqual(values,self.H.data.values())

	def test_multiple_entry_heap_5_update(self):
		self.H.update('G',8)
		self.check_heap_order_property()
		self.H.update('E',0)
		self.check_heap_order_property()
		self.H.update('E',9)
		self.check_heap_order_property()
		self.H.update('F',2)
		self.check_heap_order_property()
		self.H.update('G',2)
		self.H.update('E',6)
		self.H.update('F',5)
		self.check_heap_order_property()

	def test_multiple_entry_heap_6_pop(self):	
		heap_sorted = []
		while not self.H.isEmpty():
			heap_sorted.append(self.H.pop())
		self.assertEqual(heap_sorted,sorted(self.data,key=lambda (x,y): y))
		self.check_assertions([],{},0)


if __name__ == "__main__":
	print '\n[PROCESS]: Running Tests...'
	suite = unittest.TestLoader().loadTestsFromTestCase(MinHeapTest)
	testExecutor = unittest.TextTestRunner(verbosity=2).run(suite)
	if testExecutor.wasSuccessful(): print '[PROCESS]: Tests Completed.\n'
	else: print '[PROCESS]: Tests Aborted.\n'
