from trees.trees import *

def k_ary(root):
        """
        Input: root
        Output: list of items thats tree contains
        """
        k_ary_Queue = Queue()
        k_ary_Queue.enqueue(root)

        list_tree = []
        while k_ary_Queue.peek():
            Front_Node = k_ary_Queue.dequeue()
            list_tree += [Front_Node.value]
            if Front_Node:
                for node in Front_Node.left:
                    k_ary_Queue.enqueue(node)
        return list_tree

def fizz_buzz_checker(node):
    if not node.value % 5 and not node.value % 3:
        return "FizzBuzz"
    elif not node.value % 3:
        return "Fizz"
    elif not node.value % 5:
        return "Buzz"
    else:
        return str(node.value)

def fizz_buzz_tree(root):
    """
    Arguments: k-ary tree
    Return:  new k-ary tree
    """
    Fizz_Buzz_Queue = Queue()
    Fizz_Buzz_Queue.enqueue(root)

    while Fizz_Buzz_Queue.peek():
        Front_Node = Fizz_Buzz_Queue.dequeue()
        Front_Node.value = fizz_buzz_checker(Front_Node)
        for item in Front_Node.left and item in Front_Node.right:
            Fizz_Buzz_Queue.enqueue(item)
    return k_ary(root)

if __name__=="__main__":
    pass
