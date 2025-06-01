import math

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
    return True

print(is_prime(11))

print(is_prime(9))