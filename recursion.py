def fac(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if number == 0:
        return 1
    return number * fac(number - 1)


'''
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''
def digital_root(n):
    if n // 10 == 0:
        return n
    else:
        return digital_root(digital_root(n % 10) + digital_root(n // 10))