"""Find and display the minimum values in a BST and an AVL tree."""

from binary_tree import BinaryTree
from avl_tree import AVLTree
from utils import seed_tree


if __name__ == "__main__":
    values = [10, 5, 20, 3, 7, 30]

    bt = seed_tree(BinaryTree(), values)
    avl = seed_tree(AVLTree(), values)

    print("Binary tree minimum:", bt.find_min())
    print("AVL tree minimum:", avl.find_min())
