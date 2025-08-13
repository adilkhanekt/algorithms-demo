def wave_sort(a):
    length = len(a)
    for i in range(0, length, 2):
        even_digit = a[i]
        if i != 0:    
            odd_lower = a[i-1]
        else:
            odd_lower = None
        if odd_lower and even_digit < odd_lower:
            a[i] = odd_lower
            a[i-1] = even_digit
    for i in range(1, length, 2):
        odd_digit = a[i]   
        even_lower = a[i-1]
        if even_lower < odd_digit:
            a[i] = even_lower
            a[i-1] = odd_digit
    return a

# sample = [1,2,3,4,5,6,7,8,9]
# sample = [9,8,7,6,5,4,3,2,1]
# sample = [14,23,53,66,1,22,31,54,75,13]
sample = [23,45,24,65,44,33,55,44,55,123,64,23,4235,6436,34,22,246]

new = wave_sort(sample)

print(new)
