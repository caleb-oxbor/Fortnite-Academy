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
                print("Already exists!")
                return

        new_node.parent = parent
        if parent is None:
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
        if x.parent is None:
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
        if x.parent is None:
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

    def calculate_tree_avg_kd(self, mode):
        total_count, total_sum = self._calculate_tree_sum_kd(self.root, mode)
        if total_count == 0:
            return 0
        return round((total_sum / total_count), 2)

    def _calculate_tree_sum_kd(self, node, mode):
        if node is None or node == self.nil:
            return 0, 0

        left_count, left_sum = self._calculate_tree_sum_kd(node.left, mode)
        right_count, right_sum = self._calculate_tree_sum_kd(node.right, mode)

        total_count = left_count + right_count + 1
        total_sum = left_sum + right_sum + node.player.kd[mode]

        return total_count, total_sum

    def calculate_tree_avg_wr(self, mode):
        total_count, total_sum = self._calculate_tree_sum_wr(self.root, mode)
        if total_count == 0:
            return 0
        return round((total_sum / total_count), 2)

    def _calculate_tree_sum_wr(self, node, mode):
        if node is None or node == self.nil:
            return 0, 0

        left_count, left_sum = self._calculate_tree_sum_wr(node.left, mode)
        right_count, right_sum = self._calculate_tree_sum_wr(node.right, mode)

        total_count = left_count + right_count + 1
        total_sum = left_sum + right_sum + node.player.wr[mode]

        return total_count, total_sum

    def tree_search_recurse(self, node, name, return_just_name):
        if node == self.nil or name == node.player.name:
            if return_just_name:
                return node.player
            else:
                return node

        if name < node.player.name:
            return self.tree_search_recurse(node.left, name, return_just_name)
        else:
            return self.tree_search_recurse(node.right, name, return_just_name)

    def tree_search(self, name, return_just_name=True):
        return self.tree_search_recurse(self.root, name, return_just_name)

    def remove(self, name):
        node = self.tree_search(name, False)
        if node is None or node == self.nil:
            print("Player not in dataset!")
            return

        self.remove_node(node)

    def remove_node(self, node):
        if node is None or node == self.nil:
            return

        if node.left != self.nil and node.right != self.nil:
            # Node has two children
            successor = self.find_successor(node.right)
            node.player = successor.player
            self.remove_node(successor)
        else:
            # Node has at most one child
            child = node.left if node.left != self.nil else node.right
            self.transplant(node, child)

            if not node.red:
                self.fix_delete(child)

    def find_successor(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def fix_delete(self, node):
        while node != self.root and not node.red:
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.red:
                    sibling.red = False
                    node.parent.red = True
                    self.rotate_left(node.parent)
                    sibling = node.parent.right

                if not sibling.left.red and not sibling.right.red:
                    sibling.red = True
                    node = node.parent
                else:
                    if not sibling.right.red:
                        sibling.left.red = False
                        sibling.red = True
                        self.rotate_right(sibling)
                        sibling = node.parent.right

                    sibling.red = node.parent.red
                    node.parent.red = False
                    sibling.right.red = False
                    self.rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.red:
                    sibling.red = False
                    node.parent.red = True
                    self.rotate_right(node.parent)
                    sibling = node.parent.left

                if not sibling.right.red and not sibling.left.red:
                    sibling.red = True
                    node = node.parent
                else:
                    if not sibling.left.red:
                        sibling.right.red = False
                        sibling.red = True
                        self.rotate_left(sibling)
                        sibling = node.parent.left

                    sibling.red = node.parent.red
                    node.parent.red = False
                    sibling.left.red = False
                    self.rotate_right(node.parent)
                    node = self.root

        node.red = False

    def get_highest_unicode(self, node):
        while node.right != self.nil:
            node = node.right
        return node.player

    def get_highest(self):
        if self.root is None:
            return None
        return self.get_highest_unicode(self.root)


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

        return round((total_sum / self.count), 2)

    def get_higher_unicode(self, str1, str2):
        for char1, char2 in zip(str1, str2):
            if ord(char1) < ord(char2):
                return str2
            elif ord(char1) > ord(char2):
                return str1
        if len(str1) < len(str2):
            return str2
        return str1

    def get_highest_unicode(self):
        cur_name = ""
        cur = None
        for bucket in self.table:
            for player in bucket:
                if self.get_higher_unicode(cur_name, player.name) == player.name:
                    cur_name = player.name
                    cur = player
        return cur
