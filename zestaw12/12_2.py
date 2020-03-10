# Napisać wersję rekurencyjną wyszukiwania binarnego.

# def binary_search(L, left, right, y):

#     while left <= right:
#         k = (left+right)/2
#         if y == L[k]:
#             return k
#         if y > L[k]:
#             left = k+1
#         else:
#             right = k-1
#     return None


def binarne_rek(L, left, right, y):

    try:
        if left > right:
            return None

        else:
            k = (left+right)//2

        if L[k] == y:
            return k

        else:
            if y > L[k]:
                return binarne_rek(L, k+1, right, y)
            else:
                return binarne_rek(L, left, k-1, y)

    except IndexError as error:
        print("Index Error")


L = [0, 1, 3, 5, 6, 7]

print(binarne_rek(L, 0, 6, 3))
