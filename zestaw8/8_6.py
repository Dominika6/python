# Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j).
# Porównać z wersją rekurencyjną programu. Wskazówka: Wykorzystać tablicę dwuwymiarową (np. słownik)
# do przechowywania wartości funkcji. Wartości w tablicy wypełniać kolejno wierszami.

# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.


def funkcja_p(i, j):

    tab = [[0 for x in range(i)] for y in range(j)]
    tab[0][0] = 0.5

    for x in range(1, i):
        tab[x][0] = 0.0

    for y in range(1, j):
        tab[0][y] = 1.0

    for x in range(1, i):
        for y in range(1, j):
            tab[x][y] = 0.5 * (tab[x-1][y] + tab[x][y-1])

    return tab


tablica = funkcja_p(10, 10)

print(tablica[3][2])
