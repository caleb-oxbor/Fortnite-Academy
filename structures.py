# RB tree is based off of https://blog.boot.dev/python/red-black-tree-python/
# very similar structure, but stores player objects instead of integers

class Node:
    def __init__(self, player=None):
        self.red = False
        self.parent = None
        self.left = None
        self.right = None
        self.player = player


class RedBlackTree:
    def __init__(self):
        self.nil = Node()
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, player):
        new_node = Node(player)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        cur = self.root
        while cur != self.nil:
            parent = cur
            if new_node.player.name < cur.player.name:
                cur = cur.left
            elif new_node.player.name > cur.player.name:
                cur = cur.right
            else:
                return

        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.player.name < parent.player.name:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:

                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    def calculate_tree_avg(self):
        total_count, total_sum = self._calculate_tree_sum(self.root)
        if total_count == 0:
            return 0
        return total_sum / total_count

    def _calculate_tree_sum(self, node):
        if node is None or node == self.nil:
            return 0, 0

        left_count, left_sum = self._calculate_tree_sum(node.left)
        right_count, right_sum = self._calculate_tree_sum(node.right)

        total_count = left_count + right_count + 1
        total_sum = left_sum + right_sum + node.player.kd_solo

        return total_count, total_sum


class HashMap:
    def __init__(self, initial_size=10):
        self.size = initial_size
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        self.load_factor_threshold = 0.7

    def hash_function(self, key):
        base = 31
        mod = self.size
        hash_value = 0
        for char in key:
            hash_value = (hash_value * base + ord(char)) % mod
        return hash_value

    def insert(self, player):
        if self.load_factor() > self.load_factor_threshold:
            self.resize()

        index = self.hash_function(player.name)
        bucket = self.table[index]
        for i, entry in enumerate(bucket):
            if entry.name == player.name:
                bucket[i] = player  # Update existing player
                return
        bucket.append(player)
        self.count += 1

    def load_factor(self):
        return self.count / self.size

    def resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        old_count = self.count
        self.count = 0
        for bucket in old_table:
            for player in bucket:
                self.insert(player)

    def get(self, key):
        index = self.hash_function(key)
        for player in self.table[index]:
            if player.name == key:
                return player
        return None

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]
        for i, player in enumerate(bucket):
            if player.name == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def calculate_hashmap_avg(self):
        total_sum = 0
        for bucket in self.table:
            for player in bucket:
                total_sum += player.kd_solo

        return total_sum / self.count

