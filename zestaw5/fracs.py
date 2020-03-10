# Zestaw nr 5, Dominika Jadach


##################################################
def add_frac(frac1, frac2):        # frac1 + frac2
    if frac1[1] == frac2[1]:
        return[frac1[0]+frac2[0], frac1[1]]
    else:
        return[(frac1[0] * frac2[1]) + (frac2[0] * frac1[1]), frac1[1] * frac2[1]]


def sub_frac(frac1, frac2):         # frac1 - frac2
    if frac1[1] == frac2[1]:
        return [frac1[0] - frac2[0], frac1[1]]
    else:
        return [(frac1[0] * frac2[1]) - (frac2[0] * frac1[1]), frac1[1] * frac2[1]]


def mul_frac(frac1, frac2):         # frac1 * frac2
    return [frac1[0] * frac2[0], frac1[1] * frac2[1]]


def div_frac(frac1, frac2):         # frac1 / frac2
    return [(frac1[0] * frac2[1]), (frac1[1] * frac2[0])]


def is_positive(frac):              # bool, czy dodatni
    if frac[0] > 0 and frac[1] > 0:
        return True
    elif frac[0] < 0 and frac[1] < 0:
        return True
    else:
        return False


def is_zero(frac):                  # bool, typu [0, x]
    if frac[0] == 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    if frac2float(frac1) < frac2float(frac2):
        return 1
    elif frac2float(frac1) > frac2float(frac2):
        return -1
    else:
        return 0


def frac2float(frac):               # konwersja do float
    return float(frac[0]) / float(frac[1])
