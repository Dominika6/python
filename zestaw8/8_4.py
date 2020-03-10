# Zaimplementować algorytm obliczający pole powierzchni trójkąta,
# jeżeli dane są trzy liczby będące długościami jego boków.
# Jeżeli podane liczby nie spełniają warunku trójkąta, to program ma generować wyjątek ValueError.
import math


def heron(a, b, c):

    if a >= b + c or b >= a + c or c >= a + b:
        raise ValueError("ValueError")

    p = (a + b + c) / 2
    s = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print("Pole trojkata = ", s)


heron(3, 4, 5)
