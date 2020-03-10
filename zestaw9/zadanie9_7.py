# zadanie 9.7
# Dla drzewa BST napisać funkcje znajdujące największy i najmniejszy element przechowywany w drzewie.
# Mamy łącze do korzenia, nie ma klasy BinarySearchTree. Drzewo BST nie jest modyfikowane,
# a zwracana jest znaleziona wartość (węzeł). W przypadku pustego drzewa należy wyzwolić wyjątek ValueError.


class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if self.data > node.data:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        elif self.data < node.data:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        else:
            pass


def bst_max(top: Node):
    if top is None:
        raise ValueError("ValueError")
    current = top
    while current.right is not None:
        current = current.right
    return current


def bst_min(top: Node):
    if top is None:
        raise ValueError("Binary Search Tree is empty.")
    current = top
    while current.left is not None:
        current = current.left
    return current
