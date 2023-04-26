#Exercício 4 - b)

class Category:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def find_subcategories(self, category):
        subcategories = []

        def traverse(node):
            if node != None:
                for child in node.children:
                    if child == category:
                        subcategories.extend(child.children)
                    traverse(child)

        traverse(self.root)

        return subcategories

eletronicos = Category("Eletrônicos")
computadores = Category("Computadores")
tablets = Category("Tablets")
smartphones = Category("Smartphones")
laptops = Category("Laptops")
desktops = Category("Desktops")
eletronicos.add_child(computadores)
eletronicos.add_child(tablets)
eletronicos.add_child(smartphones)
computadores.add_child(laptops)
computadores.add_child(desktops)

ecommerce_tree = BinaryTree(root=eletronicos)