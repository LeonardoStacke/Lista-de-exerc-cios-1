#Exercício 4 - a)

class Node:
    def __init__(self, name, father=None, mother=None):
        self.name = name
        self.father = father
        self.mother = mother

    def __str__(self):
        return self.name

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def find_relationship(self, person1, person2):
        def is_descendant(person, ancestor):
            if person == None:
                return False
            elif person == ancestor:
                return True
            else:
                return is_descendant(person.father, ancestor) or is_descendant(person.mother, ancestor)

        if person1 == person2:
            return "same person"
        elif is_descendant(person1, person2):
            return "descendant"
        elif is_descendant(person2, person1):
            return "ancestor"
        else:
            return "unrelated"

joao = Node("Joao")
maria = Node("Maria")
bruna = Node("Bruna")
carlos = Node("Carlos", father=joao, mother=maria)
paulo = Node("Paulo", father=carlos, mother=bruna)

family_tree = BinaryTree(root=paulo)
