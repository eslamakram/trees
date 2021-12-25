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
    if node%15 == 0:
        return "FizzBuzz"
    elif node % 3 == 0:
        return "Fizz"
    elif node % 5 == 0:
        return "Buzz"
    else:
        return str(node)

def fizz_buzz_tree(self,root):
    """
    Arguments: k-ary tree
    Return:  new k-ary tree
    """
    output = []
    Fizz_Buzz_tree = self.pre_order(root)
    if self.root is None:
        return "tree is empty"
    else:

      for i in  Fizz_Buzz_tree:
          i = fizz_buzz_checker(i)
          output.append(i)
       
    return output

if __name__=="__main__":
    pass
