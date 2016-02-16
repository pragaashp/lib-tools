import java.util.Arrays;
import java.util.ArrayList;
import java.util.Stack;
import java.util.HashMap;

public class BSTree<E> {
	
	public BSTNode root;
	private int keys;

	public BSTree()
	{
		root = null;
		keys = 0;
	}

	public void insert(E data)
	{
		if (root == null)
		{
			root = new BSTNode(data,null,null);
		}
		else
		{
			boolean inserted = false;
			BSTNode n = this.root;
			while (!inserted)
			{
				if ( ((Comparable)data).compareTo((Comparable)n.key) < 0)
				{
					if (n.hasLeftChild())
						n = n.leftChild;
					else
					{
						n.leftChild = new BSTNode(data,null,null);
						inserted = true;
					}
				}
				else
				{
					if (n.hasRightChild())
						n = n.rightChild;
					else
					{
						n.rightChild = new BSTNode(data,null,null);
						inserted = true;
					}
				}
			}
		}
		keys++;
	}

	public Integer[] recursiveTraverse()
	{
		ArrayList<E> list = new ArrayList<E>(this.keys);
		this.__rectraverse(this.root,list);
		Integer[] result = new Integer[list.size()];
		return list.toArray(result);
	}

	private void __rectraverse(BSTNode n, ArrayList<E> alist)
	{
		if (n.hasLeftChild())
			this.__rectraverse(n.leftChild,alist);

		alist.add((E)n.key);

		if (n.hasRightChild())
			this.__rectraverse(n.rightChild,alist);
	}

	public Integer[] iterativeTraverse()
	{
		Stack<BSTNode> stack = new Stack<BSTNode>();
		ArrayList<E> list = new ArrayList<E>(this.keys);

		BSTNode n = this.root;
		while (n.hasLeftChild())
		{
			stack.push(n);
			n = n.leftChild;
		}
		stack.push(n);
		while (!stack.empty())
		{
			n = stack.pop();
			list.add((E)n.key);
			if (n.hasRightChild())
			{
				n = n.rightChild;
				while (n.hasLeftChild())
				{
					stack.push(n);
					n = n.leftChild;
				}
				stack.push(n);
			}
		}
		Integer[] result = new Integer[list.size()];
		return list.toArray(result);
	}

	public int maximumSumPath()
	{	
		if (this.root != null)
			return this.__findMSP(this.root)[2];
		else
			return -1;
	}

	private int[] __findMSP(BSTNode n)
	{
		int[] nodeSums = {(int)n.key,(int)n.key,0}, leftSums = {0,0,0}, rightSums = {0,0,0};
		if (n.hasLeftChild())
		{
			leftSums = this.__findMSP(n.leftChild);
			nodeSums[0] += Math.max(leftSums[0],leftSums[1]);
		}
		if (n.hasRightChild())
		{
			rightSums = this.__findMSP(n.rightChild);
			nodeSums[1] += Math.max(rightSums[0],rightSums[1]);
		}
		nodeSums[2] = Math.max(nodeSums[0]+nodeSums[1]-(int)n.key,Math.max(leftSums[2],rightSums[2]));
		return nodeSums;
	}

	public static void main(String[] args)
	{
		BSTree T = new BSTree<Integer>();
		Integer[] keys = {15,2,1,0,8,7,5,4,3,6,13,9,11,10,12,14,16,18,17,19};
		for (Integer k : keys)
			T.insert(k);

		Arrays.sort(keys);
		if ( Arrays.equals(T.recursiveTraverse(),keys) )
			System.out.println("RECURSIVE: SUCCESS!");
		if ( Arrays.equals(T.iterativeTraverse(),keys) )
			System.out.println("ITERATIVE: SUCCESS!");

		System.out.println("Maximum Sum Path: " + T.maximumSumPath());
	}
}