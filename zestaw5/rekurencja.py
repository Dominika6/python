# Zestaw nr 5, Dominika Jadach


##################################################
def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


#####################################################
def fibonacci(n):
    if n == 1:
        return 1
    else:
        a = 1
        b = 1
        c = 0
        for i in range(n - 1):
            c = c + a
            a = b
            b = c
        return c



