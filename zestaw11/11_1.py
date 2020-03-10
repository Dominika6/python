# Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. 

import random
import math

# (a) różne liczby int od 0 do N-1 w kolejności losowej,
def losowy_int(n):
    L = [i for i in range(n)]
    random.shuffle(L)
    return L


print(losowy_int(7))


# (b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
def prawie_posortowane(n):
    L = []
    for i in range(n):
        if i == (n - 1) and (i % 2 == 0):
            L.append(i)
            return L
        elif (i % 2) == 0:
            L.append(i+1)
        elif (i % 2) == 1:
            L.append(i-1)
    return L


print(prawie_posortowane(7))


# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
def prawie_posortowane_odwrotnie(n):
    return prawie_posortowane(n)[::-1]


print(prawie_posortowane_odwrotnie(7))


# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
def float_gauss(n):
    return [random.gauss(0, 1) for i in range(n)]


print(float_gauss(7))


# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N)
def losowe_powtarzajace(n):
    return [random.randint(0, int(math.sqrt(n))) for i in range(n)]


print(losowe_powtarzajace(7))
