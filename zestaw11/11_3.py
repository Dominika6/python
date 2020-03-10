# Poprawić wybrany algorytm sortowania, aby przyjmował jako dodatkowy argument funkcję porównującą elementy na liście

"""
funkcja do przerobienia:

def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        swap(L, i, k)
"""


def porownanie(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def selectsort_poprawiony(L, left, right, funkcja=porownanie):
    for i in range(left, right):
        k = i
        for j in range(i + 1, right + 1):
            if funkcja(L[j], L[k]) == -1:  # L[j] < L[k]
                k = j
        swap = L[i]
        L[i] = L[k]
        L[k] = swap


L = [2, 4, 0, 6, 8, 3, 1]
print("przed sortowaniem:\t", L)
selectsort_poprawiony(L, 0, 6, porownanie)
print("po sortowaniu:\t\t", L)
