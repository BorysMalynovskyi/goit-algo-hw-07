"""Shared helper functions for tree tasks."""


def seed_tree(tree, values):
    """Insert a list of values into any tree that exposes insert()."""
    for value in values:
        tree.insert(value)
    return tree
