class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self,value):
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
            if not self.front :
                raise Exception('Queue is Empty')

            if self.front==self.rear:
                temp=self.front
                self.front=None
                self.rear=None
                return temp.value
            else:
                temp=self.front
                self.front=self.front.next
                temp.next=None
                return temp.value

    def peek(self):
        if not self.front:
            raise Exception('Queue is empty...')
        return self.front.value



class Binary_Tree:
     def __init__(self):
         self.root = None
         self.output = []

     def pre_order(self, root):
                """
                node=> left=> right =>
                """
                try:
                    self.output.append(root.value)
                    if root.left is not None:
                        self.pre_order(root.left)
                    if root.right is not None:
                        self.pre_order(root.right)
                    return self.output
                except:
                  raise Exception("Error  with pre_order!!! ")

     def in_order(self,root):
         """
         left=> node=> right =>
         """
         try:
                if root.left is not None:
                    self.in_order(root.left)

                self.output.append(root.value)

                if root.right is not None:
                    self.in_order(root.right)
                return self.output

         except:
            raise Exception("Error  with in_order!!! ")

     def post_order(self,root):
         """
         left=> right=> node =>
         """
         try:

                if root.left is not None:
                    self.post_order(root.left)

                if root.right is not None:
                    self.post_order(root.right)

                self.output.append(root.value)
                return self.output

         except:
            raise Exception("Error  with post_order!!! ")

     def tree_max(self, root = None):
            """
            find maximum value
            Returns: number
            """
            try:

                #Check whether tree is empty Base case
                if(root == None):
                    print("Tree is empty")
                    return 0

                else:
                    #Variable maximum will store temp's data
                    maximum = root.value

                    #It will find largest element in left subtree
                    if(root.left != None):
                        leftMax = self.tree_max(root.left)
                        #Compare variable maximum with leftMax and store greater value into maximum
                        maximum = max(maximum, leftMax)

                    #It will find largest element in right subtree
                    if(root.right != None):
                        rightMax = self.tree_max(root.right)
                        #Compare variable maximum with rightMax and store greater value into maximum
                        maximum = max(maximum, rightMax)

                    return maximum

            except:
              raise Exception("Error with tree max!!! ")

     def Breadth_First(self,root):
            """
            Input: tree
            Output: list of all values in the tree, in the order they were encountered
            """
            if not root:
                        raise Exception("Tree is empty")

            Breadth_First_Queue = Queue()
            Breadth_First_Queue.enqueue(root)

            try:
                    while Breadth_First_Queue.peek():

                            Front_Node = Breadth_First_Queue.dequeue()

                            self.output.append(Front_Node.value)

                            if Front_Node.left:
                                Breadth_First_Queue.enqueue(Front_Node.left)

                            if Front_Node.right:
                                Breadth_First_Queue.enqueue(Front_Node.right)
            except:
                return self.output
                # raise Exception("Error  with Breadth First!!! ")
class Binary_Search_Tree(Binary_Tree):
      def Add(self, value):
            """
            Add Method:
                Arguments: value
                Return: nothing
                Adds a new node with that value in the correct location in the binary search tree.
            """
            if not self.root:
                self.root = Node(value)
                return

            current = self.root

            while current:
                if value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        return

                else:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        return

      def Contains(self,value):
            """
            Contains:
                Argument: value
                Returns: boolean indicating whether or not the value is in the tree at least once.
            """
            if not self.root:
                raise Exception("TREE IS EMPTY")
            elif value == self.root.value:
                return True
            else:
                current = self.root
                while current:

                    if current.value < value:

                        if current.right:
                            current = current.right
                            if value == current.value:
                                return True
                        else:
                            return False

                    else:

                        if current.left:
                            current = current.left
                            if value == current.value:
                                return True
                        else:
                            return False



