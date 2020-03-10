# Obliczyć liczbę pi za pomocą algorytmu Monte Carlo.
# Wykorzystać losowanie punktów z kwadratu z wpisanym kołem.
# Sprawdzić zależność dokładności wyniku od liczby losowań.
# Wskazówka: Skorzystać z modułu random.
import random
import math


def calc_pi(n=100):
    luck = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # d = odleglosc wylosowanego punktu od srodka okregu
        d = math.sqrt(x * x + y * y)
        if d <= 1:
            luck += 1
    return luck


pi = 4 * calc_pi() / 100
print("Przyblizenie liczby pi: ", pi)
