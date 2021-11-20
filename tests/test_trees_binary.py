"""
Can successfully instantiate an empty tree
Can successfully instantiate a tree with a single root node
Can successfully add a left child and right child to a single root node
Can successfully return a collection from a preorder traversal
Can successfully return a collection from an inorder traversal
Can successfully return a collection from a postorder traversal
"""
from trees.trees import Node , Binary_Tree, Binary_Search_Tree
import pytest

@pytest.fixture
def tree_test_data():
    root=Node("A")
    root.left=Node("B")
    root.right=Node("C")
    root.left.left=Node("D")
    root.left.right=Node("E")
    root.right.left=Node("F")
    return root

def test_empty_tree():
    tree = Binary_Tree()
    actual = tree.root
    expected = None
    assert actual == expected

def test_tree_single_root_node():
     tree = Binary_Tree()
     tree.root = Node('root')
     actual = tree.root.value
     expected ='root'
     assert actual == expected


def test_preorder_traversal(tree_test_data):
    tree = Binary_Tree()
    actual = tree.pre_order(tree_test_data)
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    assert actual == expected

def test_inorder_traversal(tree_test_data):
    tree = Binary_Tree()
    actual = tree.in_order(tree_test_data)
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    assert actual == expected

def test_postorder_traversal(tree_test_data):
    tree = Binary_Tree()
    actual = tree.post_order(tree_test_data)
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    assert actual == expected

