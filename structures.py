# based off of https://blog.boot.dev/python/red-black-tree-python/
from player import Player
class Node:
    def __init__(self, player=None):
        self.red = False
        self.parent = None
        self.left = None
        self.right = None
        self.player = player

class RB_Tree:
    def __init__(self):
        self.nil = Node()
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
