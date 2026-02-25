#!/usr/bin/env python3
"""
My module document
"""

import numpy as np


class Node:
    """
    Node class
    """
    def __init__(self, feature=None, threshold=None,
                 left_child=None, right_child=None, is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """
        max_depth_below function
        """
        left = self.left_child.max_depth_below()
        right = self.right_child.max_depth_below()
        return max(left, right)

    def count_nodes_below(self, only_leaves=False):
        """
        count_nodes_below function
        """
        count = 0

        if not only_leaves:
            count = 1

        if self.left_child is not None:
            count += self.left_child.count_nodes_below(only_leaves)

        if self.right_child is not None:
            count += self.right_child.count_nodes_below(only_leaves)

        return count

    def left_child_add_prefix(self, text):
        """
        left_child_add_prefix function
        """
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"

        for x in lines[1:]:
            if x:
                new_text += "    |  " + x + "\n"

        return new_text

    def right_child_add_prefix(self, text):
        """
        right_child_add_prefix function
        """
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"

        for x in lines[1:]:
            if x:
                new_text += "       " + x + "\n"

        return new_text

    def __str__(self):
        """
        __str__ function
        """
        label = "root" if self.is_root else "node"
        res = f"{label} [feature={self.feature}, threshold={self.threshold}]\n"

        if self.left_child:
            res += self.left_child_add_prefix(self.left_child.__str__())

        if self.right_child:
            res += self.right_child_add_prefix(self.right_child.__str__())

        return res.rstrip()


class Leaf(Node):
    """
    Leaf class
    """
    def __init__(self, value, depth=None):
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """
        max_depth_below function
        """
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """
        count_nodes_below function
        """
        return 1

    def __str__(self):
        """
        __str__ function
        """
        return f"-> leaf [value={self.value}]"


class Decision_Tree:
    """
    Decision_Tree class
    """
    def __init__(self, max_depth=10, min_pop=1,
                 seed=0, split_criterion="random", root=None):
        self.rng = np.random.default_rng(seed)

        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)

        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """
        depth function
        """
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """
        count_nodes function
        """
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        """
        __str__ function
        """
        return self.root.__str__()
