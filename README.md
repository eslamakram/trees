# Binary Tree and BST Implementation

1. Build Binary_Tree class Define a method for each of the depth first traversals:
         * pre-order
         * in-order
         * post-order
which returns an array of the values, ordered appropriately.

2. Create a Binary Search Tree class Define methods :
         *Add
         * Contains

## Approach & Efficiency

pre-order: time O(n), space O(n)
in-order: time O(n), space O(n)
post-order: time O(n), space O(n)
Add: time O(logn), space O(1)
Contains: time O(logn), space O(1)

### API

pre-order: method that return tree in order: node=> left=> right =>
in-order: method that return tree in order: left=> node=> right =>
post-order: method that return tree in order: left=> right=> node =>
Add: to add a value to a tree by binary search algorithm
Contains: to check if the tree contains a value

# Challenge Max Tree

Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process

![ch16](ch16.png)

## Approach & Efficiency

 i used recursion approach to  find out the largest node in the given binary tree. i first defined variable max that holds root's data. Then, we traverse through the left sub-tree to find the largest node. Compare it with max and store the maximum of two in a variable max. Then, we traverse through the right subtree to find the largest node and compare it with max. In the end, max will have the largest node.

- time complexity: O(n)
- space complexity: O(1)

## Solution

```python

def tree_max(self, root):
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
```

# challange : Breadth First tree

Write a function called breadth first
Arguments: tree
Return: list of all values in the tree, in the order they were encountered

## Whiteboard Process

![ch17](CH7.drawio.png)

## Approach & Efficiency

 i used iteration  approach to  travrese all nodes in the given binary tree.

- time complexity: O(n)
- space complexity: O(n)

## Solution

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

## Fizz Buzz Tree Challenge

Conduct ???FizzBuzz??? on a binaryTree while traversing through it. Change the values of each of the nodes dependent on the current node???s value

## Approach & Efficiency

- Write a function called FizzBuzzTree which takes a binaryTree as an argument.
- Without utilizing any of the built-in methods available to your language, determine weather or not the value of each
 node is divisible by 3, 5 or both, and change the value of each of the nodes:
  - If the value is divisible by 3, replace the value with ???Fizz???
  - If the value is divisible by 5, replace the value with ???Buzz???
  - If the value is divisible by 3 and 5, replace the value with ???FizzBuzz???
     Return the binaryTree with its new values.

For explicitly-typed languages: Ensure your node values are of type Object, to hold either strings or integers.

## Solution

[Code](../trees/tree_fizz_buzz.py) | [Tests](../trees/tests/test_tree_fizz_buzz.py)

![WhiteBoard]()

## Checklist

- [x] Top-level README ???Table of Contents??? is updated
- [x] Feature tasks for this challenge are completed
- [x] Unit tests written and passing
  - [-] ???Happy Path??? - Expected outcome
  - [x] Expected failure
  - [x] Edge Case (if applicable/obvious)
- [x] README for this challenge is complete
  - [x] Summary, Description, Approach & Efficiency, Solution
  - [x] Link to code
  - [x] Picture of whiteboard
