"""
Overview:
* There is a heap of n bones
* Both players have to pick up 1, 2, or 3 bones in their turn
* A player who can't pick up any bones loses the game
"""

# Leave for testing
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from util.minimax import Minimax
from util.structures import Node, Tree


class BonesNode(Node):

    def __init__(self, num_bones, is_max_player):
        super(BonesNode, self).__init__(is_max_player)
        self.num_bones = num_bones

class Bones(Minimax):

    def __init__(self):
        pass

    def get_possible_states(self, num_bones):
        possible_moves = range(1, 4)
        # print(possible_moves)
        
        possible_states = filter(lambda x: x >= 0,map(lambda x: num_bones - x, possible_moves))
        # print (possible_states)
        return possible_states

    def construct_tree(self, num_bones):
        root = BonesNode(num_bones, True)
        tree = Tree(root)
        self.__construct_tree(root)
        self.tree = tree

    # Recursively constructs tree
    def __construct_tree(self, parent_node):
        potential_heaps = self.get_possible_states(parent_node.num_bones)
        is_child_max_player = not parent_node.is_max_player
        for heap in potential_heaps:
            new_node = BonesNode(heap, is_child_max_player)
            parent_node.add_child(new_node)
            if new_node.num_bones > 0:
                self.__construct_tree(new_node)

    def check_win(self):
        root = self.tree.root
        self.__check_win(root)
        return root.score == 1

    def __check_win(self, node):
        children = node.children
        is_max_player = node.is_max_player
        for child in children:
            if child.num_bones == 0:
                child.score = 1 if is_max_player else -1
            else:
                self.__check_win(child)

        node.score = self.find_best_child_score(is_max_player, children)


game = Bones()
game.construct_tree(6)
print game.check_win()
game.construct_tree(8)
print game.check_win()
print game.tree


