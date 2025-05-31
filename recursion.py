def fac(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if number == 0:
        return 1
    return number * fac(number - 1)