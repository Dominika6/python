# Zestaw nr 3, Dominika Jadach

##################################################
# zad 3.1
"""
niepotrzebne średniki, poprawiona wersja:
x = 2; y = 3;
if (x > y):
    result = x
else:
    result = y


kod powinien być rozdzielony znakiem nowej linii
for i in "qwerty":
    if ord(i) < 100: print(i)


tutaj jest potrzebny nawias przy print
for i in "axby": print(ord(i) if ord(i) < 100 else i)
"""

##################################################
# zad 3.2
"""
niepoprawne przypisanie, funkcja sort w tym miejscu wykonuje sortowanie, nie możemy tego przypisać, poprawione:
L = [3, 5, 4]
L.sort()


zbyt dużo przypisywanych wartości, trzeba albo dodać zmienną, albo usunąć jedną z liczb, np:
x, y = 1, 2


jak zapisujemy krotkę to nie możemy jej edytować
X = 1, 2, 3 ; X[1] = 4


X[3] wychodzi poza wielkość listy
X = [1, 2, 3]; X[3] = 4


append() nie działa dla Stringów, można po połączyć znakiem "+"
X = "abc" ; X.append("d")


funkcja pow() wymaga dwóch argumentów: pow, informujemy funkcję tym o podstawie i stopniu potęgi
map(pow, range(8))
"""

##################################################
# zad 3.3

print("zadanie3: ")
for i in range(0, 31):
    if i % 3:
        print(i)

##################################################
# zad 3.4

print("\n" + "zadanie4: ")
x = input("Podaj liczbę: ")
while x:
    if not x.isdigit():
        if x == "stop":
            break
        else:
            print("To nie jest liczba! Wpisz liczbę, albo przerwij działanie programu wpisując stop. \n")
    else:
        print(x + " do potęgi trzeciej to : " + str(pow(int(x), 3)) + "\n")
    x = input("Podaj liczbę: ")

##################################################
# zad 3.5

print("zadanie5: " + "\n")


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

##################################################
# zad 3.6
# Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string,
# a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

print("\n" + "zadanie6: ")


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
# zad 3.8

print("\n" + "zadanie8: ")


def a(s1, s2):
    s3 = []
    for i in s1:
        if i in s2:
            s3.append(i)  # append dodaje element na koniec listy
    return s3


def b(s1, s2):
    s3 = []
    for i in s1:
        s3.append(i)
    for i in s2:
        if i not in s1:
            s3.append(i)
    return s3


s1 = [1, 3, 6, 7, 8]
s2 = [1, 5, 7, 9]

print("Lista elementów występujących jednocześnie w obu sekwencjach: ")
print(a(s1, s2))
print("Lista wszystkich elementów z obu sekwencji: ")
print(b(s1, s2))

##################################################
# zad 3.9

print("\n" + "zadanie9: ")


def sumy(L):
    s = []
    for seq in L:
        sum = 0
        for item in seq:
            sum += item
        s.append(sum)
    return s


L = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
print(sumy(L))

##################################################
# zad 3.10

print("\n" + "zadanie10: ")

D = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def porownanie_roman(l1, l2):
    if D[l1] <= D[l2]:
        return 0
    else:
        return 1


def roman2int(L):
    d = {}
    for i in L:
        roman = i
        sum = 0
        for j in range(len(roman) - 1):
            if (j + 1) == (len(roman) - 1):  # przypadek jak roman jest ostatnia
                sum = sum + D[roman[j + 1]]
            if porownanie_roman(roman[j], roman[j + 1]):  # gdy pierwsza roman jest większa od drugiej (dodajemy)
                sum = sum + D[roman[j]]
            else:  # gdy druga roman jest większa od drugiej (odejmujemy)
                sum = sum - D[roman[j]]
        d[i] = sum
    return d


# przykładowe liczby
L = ["IX", "XI", "IXV", "XVI", "MVI", "CXI"]

print(roman2int(L))
