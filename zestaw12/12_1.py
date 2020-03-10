# Napisać program, który na listę L wstawi n liczb wylosowanych z zakresu od 0 do k-1.
# Następnie program wylosuje liczbę y z tego samego zakresu i znajdzie wszystkie
# jej wystąpienia na liście L przy pomocy wyszukiwania liniowego. [n=100, k=10]

import random


def wyszukiwanie_liniowe(n=100, k=10):
    L = []
    for i in range(n):
        L.append(random.randint(0, k - 1))
    y = random.randint(0, k - 1)
    ilosc_wystapien = 0
    print(f'Lista: {L}')
    print(f'y = {y}')

    wystapienia = []
    m = 0
    for j in L:
        if j == y:
            wystapienia.append(m)
            ilosc_wystapien += 1
        m += 1
    if ilosc_wystapien == 0:
        print("Brak wystąpień 'y' w liście")
    else:
        print("Ilość wystąpień 'y' w liście: ", ilosc_wystapien)

    return wystapienia


print("Lista indeksów: ", wyszukiwanie_liniowe())
