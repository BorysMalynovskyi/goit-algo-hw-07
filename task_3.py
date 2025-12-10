"""Find and display the sum of all values in a BST and an AVL tree."""

from binary_tree import BinaryTree
from avl_tree import AVLTree


def seed_tree(tree, values):
    """Insert a list of values into any tree that exposes insert()."""
    for value in values:
        tree.insert(value)
    return tree


if __name__ == "__main__":
    values = [10, 5, 20, 3, 7, 30]

    bt = seed_tree(BinaryTree(), values)
    avl = seed_tree(AVLTree(), values)

    print("Binary tree sum:", bt.sum_values())
    print("AVL tree sum:", avl.sum_values())
