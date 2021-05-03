"""A custom testing library for red black trees."""

import rbtrees
import random

def generate_red_black_tree(n):
    """
    Returns a randomly generated red-black-tree with n nodes that
    supposedly meets specfications.
    
    Args:
    n (int): Number of nodes the red-black tree will have.

    Returns:
    tree (RBTree): A authenticated red-black tree instance.
    keys (list): The keys contained in above tree.
    """
    upper_bound = n + 50
    keys = random.sample(range(1, upper_bound), n)
    tree = generate_testing_tree(keys)
    return tree, keys


def generate_testing_tree(keys):
    """
    Takes a list of nodes and returns the tree of the nodes inserted
    in that order. Made for recreating parts of failed test cases to be
    used for experimentation.
    
    Args:
    keys (list): List of keys to generate a red-black tree from -
    the keys will be inserted in the given order.

    Returns:
    tree (RBTree): A red-black tree instance with the given keys.
    """
    tree = rbtrees.RBTree()
    for i in keys:
        tree.insert(i)
    return tree


def test_trees(t, n):
    """
    Creates and tests t trees with n nodes. If a tree does not pass the test it
    is printed out along with its keys for inspection and experimentation.
    """
    for i in range(t):
        tree, keys = generate_red_black_tree(n)
        if not tree.check_red_black_tree():
            print(keys)
            print(tree.root)

if __name__ == '__main__':
    test_trees(500, 70)
