"""
Can successfully instantiate an empty tree
Can successfully instantiate a tree with a single root node
Can successfully add a left child and right child to a single root node
Can successfully return a collection from a preorder traversal
Can successfully return a collection from an inorder traversal
Can successfully return a collection from a postorder traversal
"""
from trees.trees import *
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

def test_single_node_left_right_childs():
    test = Binary_Tree()
    node = Node("A")
    node.left = Node("B")
    node.right = Node("C")
    expected_left = "B"
    actual_left = node.left.value
    expected_right = "C"
    actual1_right = node.right.value
    assert expected_left == actual_left
    assert expected_right == actual1_right


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

def test_add_Binary_Search_Tree():
    tree = Binary_Search_Tree()
    tree.Add(50)
    tree.Add(10)
    tree.Add(25)
    tree.Add(5)
    tree.Add(150)
    tree.Add(30)
    tree.Add(250)
    tree.Add(15)
    tree.Add(100)
    actual = tree.in_order(tree.root)
    expected = [5, 10, 15, 25, 30, 50, 100, 150, 250]
    assert actual == expected

def test_Contains_method():
    tree = Binary_Search_Tree()
    tree.Add(50)
    tree.Add(10)
    tree.Add(25)
    tree.Add(5)
    tree.Add(150)
    tree.Add(30)
    tree.Add(250)
    tree.Add(15)
    tree.Add(100)

    assert tree.Contains(7) == False
    assert tree.Contains(5) == True
    assert tree.Contains(150) == True
    assert tree.Contains(1) == False

def test_tree_max():
  tree = Binary_Tree()
  root = Node(2)
  root.left = Node(26)
  root.right = Node(17)
  root.left.left = Node(18)
  root.left.right = Node(8)
  actual = tree.tree_max(root)
  expected = 26
  assert actual == expected

def test_tree_max_empty():
  tree = Binary_Tree()
  assert tree.tree_max() == 0

def test_Breadth_First_tree(tree_test_data):
    tree = Binary_Tree()
    actual = tree.Breadth_First(tree_test_data)
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    assert actual == expected

def test_Breadth_First_Empty():
    root=""
    tree=Binary_Tree()
    with pytest.raises(Exception,match="Tree is empty"):
     actual=tree.Breadth_First(root)
     assert actual
