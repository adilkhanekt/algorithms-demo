import time


# Switch values between 2 variables.
print("\n===== Variables switching =====")


# Method 1
var1 = 1
var2 = 2

temp = var1
var1 = var2
var2 = temp

print(var1, var2)


# Method 2
v1 = 1
v2 = 2

v1, v2 = v2, v1

print(v1, v2)


# Sorting algorithms
print("\n===== Sorting algorithms =====")


# Bubble sort
print("\n----- Bubble sort -----")

def bubble_sort(lst):
    print("Input list:", lst)
    lst_len = len(lst)
    _outer_iter_count = 0
    for i in range(lst_len):
        _outer_iter_count += 1
        _inner_iter_count = 0
        for j in range(lst_len - i - 1):
            _inner_iter_count += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            print("\tInner iteration count:", _inner_iter_count)
            print("\tInner iteration result:", lst)
        print("Outer iteration count:", _outer_iter_count)
        print("Outer iteration result:", lst)
    return lst

lst1 = [3,1,4,6,3,4,7,5,8,76,10]

_bubble_start = time.time()
bubble_sort(lst1)
_bubble_end = time.time()
print(f"Execution time: {_bubble_end - _bubble_start} seconds")


# Selection sort
print("\n----- Selection sort -----")

def selection_sort(lst):
    print("Input list:", lst)
    lst_len = len(lst)
    _outer_iter_count = 0
    for i in range(lst_len):
        _outer_iter_count += 1
        _inner_iter_count = 0
        min_value_index = i
        for j in range(i + 1, lst_len):
            _inner_iter_count += 1
            if lst[j] < lst[min_value_index]:
                min_value_index = j
            print("\tInner iteration count:", _inner_iter_count)
            print("\tInner iteration result:", lst)
        lst[i], lst[min_value_index] = lst[min_value_index], lst[i]
        print("Outer iteration count:", _outer_iter_count)
        print("Outer iteration result:", lst)
    return lst

lst2 = [3,1,4,6,3,4,7,5,8,76,10]

_selection_start = time.time()
selection_sort(lst2)
_selection_end = time.time()
print(f"Execution time: {_selection_end - _selection_start} seconds")


# Insertion sort
print("\n----- Insertion sort -----")

def insertion_sort(lst):
    print("Input list:", lst)
    lst_len = len(lst)
    _outer_iter_count = 0
    for i in range(1, lst_len):
        _outer_iter_count += 1
        _inner_iter_count = 0
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
            _inner_iter_count += 1
            print("\tInner iteration count:", _inner_iter_count)
            print("\tInner iteration result:", lst)
        lst[j + 1] = key
        print("Outer iteration count:", _outer_iter_count)
        print("Outer iteration result:", lst)
    return lst

lst3 = [3,1,4,6,3,4,7,5,8,76,10]

_insertion_start = time.time()
insertion_sort(lst3)
_insertion_end = time.time()
print(f"Execution time: {_insertion_end - _insertion_start} seconds")


# Quick sort
print("\n----- Quick sort -----")

function_exec_count = 0

def quick_sort(lst):
    global function_exec_count
    function_exec_count += 1
    print("Input list:", lst)
    lst_len = len(lst)
    if lst_len <= 1:
        return lst
    else:
        pivot = lst[0]
        left_part = [x for x in lst[1:] if x < pivot]
        right_part = [x for x in lst[1:] if x >= pivot]
        print(f"Left part: {left_part}, Right part: {right_part}, Pivot: {pivot}\n")
    return quick_sort(left_part) + [pivot] + quick_sort(right_part)

lst4 = [3,1,4,6,3,4,7,5,8,76,10]

_quick_start = time.time()
quick_sort(lst4)
_quick_end = time.time()
print("Execution count:", function_exec_count)
print(f"Execution time: {_quick_end - _quick_start} seconds")