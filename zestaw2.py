# Zadanie numer 2, Dominika Jadach
# Aby program poprawnie działał należy go umieścić w jednym folderze z plikiem 'text.txt'
# zad 2.10

print("\n" + "zad 2.10: ")
words = 0
file = open("text.txt", "r+")
for word in file.read().split():
    words = words + 1
print("Plik zawiera słów: {0}".format(words))
file.close()


##################################################
# zad 2.11

print("\n" + "zad 2.11: ")
file = open("text.txt", "r+")
for word in file.read().split():
    for w in word:
        print("{0}_".format(w), end='')
file.close()
print(' ')


##################################################
# zad 2.12

print("\n" + "zad 2.12: ")
start = ''
end = ''
file = open("text.txt", "r+")
for word in file.read().splitlines():
    words = word.split()
    if len(words) != 0:
        start = start + words[0] + ' '
        end = end + words[-1] + ' '
print('{0}'.format(start))
print('{0}'.format(end))
file.close()


##################################################
# zad 2.13

print("\n" + "zad 2.13: ")
def zlicza_litery(line):
    l = line.split()
    suma = sum([len(x) for x in l])
    return suma
line = "line"
print(zlicza_litery(line))


##################################################
# zad 2.14

print("\n" + "zad 2.14: ")
file = open("text.txt", "r+")
for line in file.read().splitlines():
    if line.split():
        longest = max(map(len, line.split()))
        print('{0}'.format(longest))
        print('{0}'.format(list(set(s for s in line.split() if len(s) == longest))))
file.close()


##################################################
# zad 2.15

print("\n" + "zad 2.15: ")
lista = [1, 2, 3, 4, 5 ]
strout = ''
for l in lista:
    strout = strout + str(l)
print('{0}'.format(strout))


##################################################
# zad 2.16

print("\n" + "zad 2.16: ")
line = "przypadkowy ciąg GvR znaków"
replaced = line.replace("GvR", "Guido van Rossum")
print("Przed: ")
print(line)
print("Po: ")
print(replaced)


##################################################
# zad 2.17

print("\n" + "zad 2.17: ")
line = 'kot pies auto zwierzę kwiatek złoto lampa pudełko'
print("Posotowane alfabetycznie: ")
print('{0}'.format(sorted(line.split(), key=str.lower)))
print("Posotowane względem długości: ")
print('{0}'.format(sorted(line.split(), key=len)))


##################################################
# zad 2.18

print("\n" + "zad 2.18: ")
print("Ilość zer w liczbie: ")
numerek = 3045670088706540003201230456789876543098
print('{0}'.format(str(numerek).count('0')))


##################################################
# zad 2.19

print("\n" + "zad 2.19: ")
list = [234, 5, 67, 96, 0]
for l in list:
    print('{0}'.format(str(l).zfill(3)))
