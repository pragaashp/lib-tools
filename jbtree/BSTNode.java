public class BSTNode {

	public Object key;
	public BSTNode leftChild;
	public BSTNode rightChild;

	public BSTNode(Object data, BSTNode left, BSTNode right)
	{
		key = data;
		leftChild = left;
		rightChild = right;
	}

	public boolean hasLeftChild()
	{
		return leftChild != null;
	}

	public boolean hasRightChild()
	{
		return rightChild != null;
	}

}