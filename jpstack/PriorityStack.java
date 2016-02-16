import java.util.Stack;

public class PriorityStack<E extends Comparable<E>> extends Stack<E> {

	private Stack<E> maxStack;
	private Stack<E> minStack;

	public PriorityStack() {
		super();
		maxStack = new Stack<E>();
		minStack = new Stack<E>();
	}

	public E push(E item) {
		E pushed_obj = super.push(item);

		// Handle Maximum Stack;
		if (!maxStack.empty() && item.compareTo(maxStack.peek()) < 0)
			maxStack.push(maxStack.peek());
		else
			maxStack.push(item);

		// Handle Minimum Stack;
		if (!minStack.empty() && item.compareTo(minStack.peek()) > 0)
			minStack.push(minStack.peek());
		else
			minStack.push(item);

		return pushed_obj;
	}

	public E pop() {
		E popped_obj = super.pop();
		maxStack.pop();
		minStack.pop();
		return popped_obj;
	}

	public E getMax() {
		return maxStack.peek();
	}

	public E getMin() {
		return minStack.peek();
	}

	public static void main(String[] args) {
		PriorityStack<Integer> pstack = new PriorityStack<Integer>();
		Integer[] keys = {0,9,1,2,10,3,4};
		for (Integer k: keys)
			pstack.push(k);
		Integer elem;
		for (int i = 0; i < 10; ++i)
		{
			if (Math.random() > 0.5)
			{
				elem = pstack.pop();
				System.out.println("Popped Element: " + elem);
			}
			else
			{
				elem = ((int)Math.floor(Math.random() * 20));
				pstack.push(elem);
				System.out.println("Pushed Element: " + elem);
			}
			System.out.println("Maximum Value in Stack: " + pstack.getMax() );
			System.out.println("Minimum Value in Stack: " + pstack.getMin() + "\n");
		}
	}

}