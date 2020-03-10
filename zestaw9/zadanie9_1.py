# Wersja poprawiona, dodałam przykład sprawdzający poprawność działania.

# zad 9.1
# Do klasy SingleList dodać nowe metody.


class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    # klasy O(N)
    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.
    # W remove_tail() trzeba odczepić ogon.

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("ValueError")

        current = self.head
        removed = self.tail

        if current == removed:
            self.head = self.tail = None
        else:
            while current.next is not self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.length -= 1
        return removed

    # klasy O(1)
    # Węzły z listy other są przepinane do listy self na jej koniec.
    # Po wykonaniu merge() lista other powinna być pusta.

    def merge(self, other):
        if self is other or other.is_empty():
            return

        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
            self.length = other.count()

        else:
            current = self.tail
            current.next = other.head
            self.tail = other.tail
            self.length += other.count()
            other.head = None
            other.tail = None

    # czyszczenie listy

    def clear(self):
        while self.count() != 0:
            self.remove_tail()


# poniżej sprawdzam poprawność na przykładzie dwóch list
# na początek tworzę funkcję wypisującą daną listę
            
    def print_list(self):
        if self.is_empty():
            return "[ ]"

        current = self.head
        lista = []

        while current:
            lista.append(str(current))
            current = current.next

        return lista


lista1 = SingleList()

lista1.insert_head(Node(3))
lista1.insert_head(Node(2))
lista1.insert_head(Node(1))
lista1.insert_tail(Node(4))
lista1.insert_tail(Node(5))
print(lista1.print_list())

lista2 = SingleList()

lista2.insert_head(Node(5))
lista2.insert_tail(Node(6))
lista2.insert_tail(Node(7))
lista2.insert_tail(Node(8))
print(lista2.print_list())

print(lista1.remove_tail()) # zwraca element usuniety
print(lista1.print_list())
print(lista2.print_list())

lista1.merge(lista2)
print(lista1.print_list())
print(lista2.print_list())
