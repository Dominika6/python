# Zestaw nr 4, Dominika Jadach

##################################################
# zad 4.2
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.

# 3.5
def rysuj(liczba):
    miarka = ""
    for i in range(liczba * 5 + 1):
        if not i % 5:
            miarka = miarka + "|"
        else:
            miarka = miarka + "."
    miarka = miarka + "\n" + "0"

    for i in range(liczba):
        przerwa = 5 - len(str(i + 1))
        for j in range(przerwa):
            miarka = miarka + " "
        miarka = miarka + str(i + 1)
    print(miarka)


liczba = input("Podaj długość miarki: ")
rysuj(int(liczba))


# 3.6
def rysuj(x, y):
    prostokat = ""
    for i in range(int(x)):
        for j in range(int(y)):
            prostokat = prostokat + "+---"
        prostokat = prostokat + "+" + "\n"
        for k in range(int(y) * 4):
            if not k % 4:
                prostokat = prostokat + "|"
            else:
                prostokat = prostokat + " "
        prostokat = prostokat + "|"
        prostokat = prostokat + "\n"
    for j in range(int(y)):
        prostokat = prostokat + "+---"
    prostokat = prostokat + "+" + "\n"
    print(prostokat)


y = input("Podaj współrzędne x: ")
x = input("Podaj współrzędne y: ")
rysuj(x, y)


##################################################
# zad 4.3
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


print(factorial(3))


##################################################
# zad 4.4
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
    a = 1
    b = 1
    c = 0
    for i in range(n - 1):
        c = c + a
        a = b
        b = c
    return c


print(fibonacci(11))


##################################################
# zad 4.5
# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanie_iteracja(L, left, right):
    if right < left:
        left = right
        right = left
    for i in range((right - left) // 2):
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_rekurencja(L, left, right):
    L[left], L[right] = L[right], L[left]
    if left < right:
        return odwracanie_rekurencja(L, left + 1, right - 1)


lista = [1, 2, 3, 4, 5, 6]
odwracanie_iteracja(lista, 1, 4)

lista1 = [1, 2, 3, 4, 5, 6]
odwracanie_rekurencja(lista1, 1, 4)

print(lista)
print(lista1)

##################################################
# zad 4.6

# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

def sum_seq(sequence):
    suma = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            suma += sum_seq(item)
        else:
            suma += item
    return suma


sekwencja = [4, (5, 6), [], [4, 5], [10]]
print(sum_seq(sekwencja))


##################################################
# zad 4.7

# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać
# do nieograniczonej głębokości. Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
#
# seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
# print flatten(seq)            # [1,2,3,4,5,6,7,8,9]

def flatten(sequence):
    flattened_list = list()
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flattened_list.extend(flatten(item)) # extend dodaje rozdzielony na znaki element na koniec listy
        else:
            flattened_list.append(item) # append dodaje element na koniec listy

    return flattened_list


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))
