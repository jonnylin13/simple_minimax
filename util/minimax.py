# minimax algorithm - decision algorithm typically used in 2-player turn based games
# The goal of the algorithm is to find the most optimal move
# Two players - one "minimizer" and one "maximizer"

"""
Base class for minimax algorithm
"""

from abc import abstractmethod


class Minimax(object):

    def __init__(self):
        pass

    @abstractmethod
    def get_possible_states(self):
        pass

    # Not sure if *args is necessary here...
    @abstractmethod
    def constructTree(self, *args):
        pass

    @abstractmethod
    def check_win(self):
        pass

    def find_best_child_score(self, is_max_player, children):
        if is_max_player:
            return max(child.score for child in children)
        else:
            return min(child.score for child in children)

    