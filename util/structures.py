"""
Base classes for Node and Tree
"""

class Node(object):
    
    def __init__(self, is_max_player):
        self.children=[]
        self.score = 0
        self.is_max_player = is_max_player

    # Not necessary
    def add_child(self, node):
        self.children.append(node)

class Tree(object):

    def __init__(self, root):
        self.root = root # of type Node

    def __str__(self):
        output = []
        for (child in self.children):

            output.append(', '.join(str(child.score)))

            if (len(child.children) > 0):
                for (grandchild in child.children):
                    output.append(', '.join(str(grandchild.score) for child in self.root.children) + '\n')
        return ', '.join(str(child.score) for child in self.root.children)