"""A custom testing library for red black trees. Hand test or use pytest"""

import helpers
import pytest
from hypothesis import given, strategies as st


@given(st.lists(st.integers(min_value=0), unique=True))
def test_rbtree(nodes):
    """
    Use pytest and hypothesis to test Red Black Tree insertions and creations.
    """
    assert helpers.generate_rbtree(nodes).check_red_black_tree()


def authenticate_trees(t, n):
    """
    Creates and tests t trees with n nodes. If a tree does not pass the test it
    is printed out along with its keys for inspection and experimentation.
    """
    for i in range(t):
        tree, keys = helpers.random_rbtree(n)
        if not tree.check_red_black_tree():
            print(keys)
            print(tree.root)


def homemade_test():
    """
    Manually test the creation and insertion of red black trees.
    No pytest/hypothesis required.
    """
    import sys

    t = int(sys.argv[1])
    n = int(sys.argv[2])
    if not t or not n:
        print("usage: <number of trees> <number of nodes per tree>")
        sys.exit()
    authenticate_trees(t, n)


if __name__ == "__main__":
    homemade_test()
