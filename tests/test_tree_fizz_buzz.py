"""
If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
If the value is not divisible by 3 or 5, simply turn the number into a String
"""

from trees.trees import *
from trees.tree_fizz_buzz import *

def test_tree_fizz_buzz():
    tree = Binary_Tree()
    tree.root=Node(15)
    tree.root.left=Node(3)
    tree.root.right=Node(4)
    tree.root.left.left=Node(12)
    tree.root.left.right=Node(30)
    tree.root.right.left=Node(95)

    actual =  fizz_buzz_tree(tree,tree.root)
    
    expected = ['FizzBuzz', 'Fizz', 'Fizz', 'FizzBuzz', '4', 'Buzz']

    assert actual == expected


