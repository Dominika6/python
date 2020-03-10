# Zbadać problem szukania rozwiązań równania liniowego postaci a * x + b * y + c = 0.
# Podać specyfikację problemu. Podać algorytm rozwiązania w postaci listy kroków, schematu blokowego,
# drzewa. Podać implementację algorytmu w Pythonie w postaci funkcji solve1(),
# która rozwiązania wypisuje w formie komunikatów.


def solve1(a, b, c):

    if (a == 0) and (b == 0):
        print("Nie ma takiej funkcji! ")
        
    elif a == 0 and b != 0:
        print("Wynikiem jest pozioma kreska y = ", float(-c) / float(b))
        
    elif a != 0 and b == 0:
        print("Wynikiem jest pionowa kreska x = ", float(-c) / float(a))
        
    elif a != 0 and b != 0:
        print("Miejsce zerowe tej funkcji: x = ", float(-c)/float(a))


solve1(0, 0, 3)
solve1(0, 2, 3)
solve1(1, 0, 3)
solve1(1, 2, 3)
