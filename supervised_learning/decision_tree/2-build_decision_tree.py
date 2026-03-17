#!/usr/bin/env python3
"""
My module document
"""

import numpy as np


class Node:
    def __init__(self, feature=None, threshold=None, left_child=None, right_child=None, is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self) :

            ####### FILL IN THIS METHOD

    def __str__(self):
        if self.is_root:
            prefix = "root"
        else:
            prefix = "node"

        result = f"{prefix} [feature={self.feature}, threshold={self.threshold}]\n"
        result += left_child_add_prefix(self.left_child.__str__())
        result += right_child_add_prefix(self.right_child.__str__())
        return result

class Leaf(Node):
    def __init__(self, value, depth=None):
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self) :
        return self.depth

    def __str__(self):
        return (f"-> leaf [value={self.value}]")

class Decision_Tree():
    def __init__(self, max_depth=10, min_pop=1, seed=0, split_criterion="random", root=None):
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

    def depth(self) :
        return self.root.max_depth_below()

    def __str__(self):
        return self.root.__str__()


 def left_child_add_prefix(text):
    lines = text.split("\n")
    new_text = "    +---> " + lines[0] + "\n"
    for x in lines[1:]:
        new_text += "    |      " + x + "\n"
    return new_text


 def right_child_add_prefix(text):
    lines = text.split("\n")
    new_text = "    +---> " + lines[0] + "\n"
    for x in lines[1:]:
        new_text += "           " + x + "\n"
    return new_text
