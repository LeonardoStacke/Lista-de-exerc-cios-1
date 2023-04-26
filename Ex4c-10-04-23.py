# Exercício 4 - c)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left == None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right

    def find_next(self, data):
        def find_smallest(node):
            while node.left != None:
                node = node.left
            return node.data

        current = self.root
        next_node = None
        while current != None:
            if data < current.data:
                next_node = current
                current = current.left
            else:
                current = current.right
        if next_node == None:
            return None
        else:
            return find_smallest(next_node.right)

movies = BinarySearchTree()
movies.insert("Top Gun")
movies.insert("Harry Potter")
movies.insert("Star Wars")
movies.insert("Interestelar")
movies.insert("Duna")
