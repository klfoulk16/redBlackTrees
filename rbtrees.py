"""Creation and maintenance of Red-Black Trees"""

class RBTree:
    """
    A Red-Black tree.
    """

    def __init__(self):
        """
        Initialize tree with root as universal NIL node.
        """
        self.nil = Node('black', None, None, None, None)
        self.root = self.nil

    def __repr__(self):
        """
        Return string representation of Red Black Tree.
        """
        return f'Tree({self.root})'

    def insert(self, key):
        """
        Insert new node in tree. 
        Assumes that key is not already present in self.
        
        Args:
        key (int): Unique key to be added to Red-Black Tree as a new node.
        """
        # create node z, with parents and children as tree.nil
        z = Node('red', key, self.nil, self.nil, self.nil)
        # insert node Z and color it red
        y = self.nil
        x = self.root
        # if the root is nil...
        if x == y:
            # set the root to be z and make z black
            self.root = z
            z.color = 'black'
        # otherwise find the right spot in the tree
        else:
            # while x is not nil (aka we've reached the bottom of the tree)
            while x != self.nil:
                # store current x in y
                y = x
                # if z is less than x, then move to the left child
                if z.key < x.key:
                    x = x.left
                # if z is greater, move to the right child
                else:
                    x = x.right
            # once you've reached the bottom of the tree, add the node
            # set z's parent to the last node you were on
            z.parent = y
            # if z is less than y, add z to the left
            if z.key < y.key:
                y.left = z
            # otherwise add it on the right
            else:
                y.right = z
            # fix any errors
            self.insert_fixup(z)

    def insert_fixup(self, z):
        """
        Resolve any conflicts created in tree after insertion.
        
        Args:
        z (node): Recently updated node to be checked for conflicts.
        """
        # check the color of z's parent, if it's red, we have some problems
        # breakpoint()
        if z.parent.color == 'red':
            # check the color of z's uncle
            # see if z is on the left of right side of it's grandparent
            if z.parent == z.parent.parent.left:
                # z is on the left, so uncle is on right
                # if the uncle is also red...
                if z.parent.parent.right.color == 'red':
                    # change the uncle and parent to black
                    z.parent.color = 'black'
                    z.parent.parent.right.color = 'black'
                    # change the grandparent to red
                    z.parent.parent.color = 'red'
                    # do we need to check that the uncle's color didn't
                    # mess something up?
                    # then repeat for the grandparent
                    self.insert_fixup(z.parent.parent)
                # if the uncle is black there are 4 possible options
                # Left Left Case
                # parent left child, z is left child of parent
                elif z == z.parent.left:
                    # right rotate grandfather
                    self.right_rotate(z.parent.parent)
                    # swap colors of former grandfather and parent
                    z.parent.color = 'black'
                    # the grandfather is now parent's right child
                    z.parent.right.color = 'red'
                # Left Right Case
                # parent left child, z right child
                elif z == z.parent.right:
                    # left rotate parent
                    self.left_rotate(z.parent)
                    # right rotate orig grandparent (which is now z's parent)
                    self.right_rotate(z.parent)
                    # z becomes black
                    z.color = 'black'
                    # grandparent (now z's right child) becomes red
                    z.right.color = 'red'
            else:
                if z.parent.parent.left.color == 'red':
                    # change the uncle and parent to black
                    z.parent.color = 'black'
                    z.parent.parent.left.color = 'black'
                    # change the grandparent to red
                    z.parent.parent.color = 'red'
                    # do we need to check that the uncle's color didn't mess
                    # something up?
                    # then repeat for the grandparent
                    self.insert_fixup(z.parent.parent)
                # right right
                elif z == z.parent.right:
                    # left rotate grandfather
                    self.left_rotate(z.parent.parent)
                    # swap colors of former grandfather and parent
                    z.parent.color = 'black'
                    # the grandfather is now parent's left child
                    z.parent.left.color = 'red'
                # Right Left Case
                # parent right child, z left child
                elif z == z.parent.left:
                    # right rotate parent
                    self.right_rotate(z.parent)
                    # left rotate orig grandparent (which is now z's parent)
                    self.left_rotate(z.parent)
                    # z becomes black
                    z.color = 'black'
                    # grandparent (now z's right child) becomes red
                    z.left.color = 'red'
            self.root.color = 'black'

    def left_rotate(self, x):
        """
        Rotate left on node x.
        
        Args:
        x (Node): Node to rotate on. x.left != self.nil
        """
        y = x.right
        # make y's left child x's right child
        x.right = y.left
        # turn y's left sub-tree into x's right sub-tree
        if y.left != self.nil:
            y.left.parent = x

        # swap x and y's parents
        y.parent = x.parent

        # set x's parent to point to y instead of x
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            # if x was on the left side of it's parent
            x.parent.left = y
        else:   # if x was on right
            x.parent.right = y

        # put x on y's left
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        """
        Rotate right on node y.

        Args:
        y (Node): Node to rotate on. y.left != self.nil
        """
        x = y.left
        # make y's left child x's right child
        y.left = x.right
        # turn x's right sub-tree into y's left sub-tree
        if x.right != self.nil:
            x.right.parent = y

        # swap x and y's parents
        x.parent = y.parent

        # set x's parent to point to y instead of x
        if y.parent == self.nil:
            self.root = x
        else:
            # if y was on the left side of it's parent
            if y == y.parent.left:
                y.parent.left = x
            else:   # if x was on right
                y.parent.right = x

        # put y on x's right
        x.right = y
        y.parent = x

    def inorder_tree_walk(self, x, keys=None):
        """
        Returns list of keys starting with left-most key
        and ending at right-most key descending from given node x.

        Args:
        x (Node): Node in Red-Black tree
        keys (list): List of keys previously traversed, else None

        Returns:
        keys (list): list of keys decending from Node x 
        """
        if keys is None:
            keys = []
        if x != self.nil:
            keys = self.inorder_tree_walk(x.left, keys)
            keys.append(x.key)
            keys = self.inorder_tree_walk(x.right, keys)
        return keys

    def check_red_black_tree(self):
        """
        Checks that all requirements of red-black tree are met.

        If a requirement is not met, a short description is printed out.

        bool: True if red-black tree requirements are met, else False.
        """
        # root and leaves (NIL) are black
        if self.root.color != 'black':
            print("Root was not black")
            return False

        # if a node is red, it's children are black
        if not self.check_red_children(self.root):
            print("Red children were not black")
            return False
        
        # keys are in sorted order
        keys = self.inorder_tree_walk(self.root)
        if not all(keys[i] < keys[i + 1] for i in range(len(keys)-1)):
            print(f"Keys were not in order: {keys}")
            return False
        # make sure no duplicate keys (rule of binary search tree)
        if len(set(keys)) != len(keys):
            print("There were duplicate keys")
            return False
        
        # all paths from node to it's descendants have same number of black nodes
        if not self.check_num_black_nodes(self.root)[0]:
            print("The number of black nodes was off")
            return False

        # make sure the NIL node is still black
        if self.nil.color != 'black':
            print("The nil node became red.")
            return False

        return True
    
    def check_red_children(self, x):
        """
        Assert that all red nodes have black children.

        Returns:
        bool: True if all red nodes have black children, else False.
        """
        if x != self.nil:
            if not self.check_red_children(x.left):
                return False
            if x.color == 'red':
                if (x.left.color == 'red') or (x.right.color == 'red'):
                    return False
            if not self.check_red_children(x.right):
                return False
        return True

    def check_num_black_nodes(self, x):
        """
        Assert that all paths from tree.root to NIL have the same number of black nodes
        
        Returns:
        bool: True if all paths from tree.root to NIL have the same number of black nodes.
        int: Number of black nodes in a given path.
        """
        # for more info: https://gist.github.com/aldur/8c061c88b0f58e871776
        if x == self.nil:
            return True, 1
        if x.color == 'red':
            blacks = 0
        else:
            blacks = 1
        l, blacks_l = self.check_num_black_nodes(x.left)
        r, blacks_r = self.check_num_black_nodes(x.right)
        return all([r, l, blacks_l == blacks_r]), blacks_r + blacks


class Node:
    """
    A node contained in the Red Black Tree.
    """

    def __init__(self, color, key, parent, left, right):
        self.color = color
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        """
        Prints out a string representation of a node.
        """
        return f'Node({self.key}, color: {self.color}, left: {self.left}, right: {self.right})'
