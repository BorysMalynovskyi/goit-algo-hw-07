"""Find and display the maximum values in a BST and an AVL tree."""

from binary_tree import BinaryTree
from avl_tree import AVLTree
from utils import seed_tree


if __name__ == "__main__":
    values = [10, 5, 20, 3, 7, 30]

    bt = seed_tree(BinaryTree(), values)
    avl = seed_tree(AVLTree(), values)

    print("Binary tree maximum:", bt.find_max())
    print("AVL tree maximum:", avl.find_max())
