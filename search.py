import time


print("--------- Linear search ---------")

lst = list(range(1,100))
item = 99

_linear_iter_count = 0

_linear_start = time.time()

for i in lst:
    _linear_iter_count += 1
    if i == item:
        print("Item is", i)
        break

_linear_end = time.time()
print(f"Iterations count: {_linear_iter_count}")
print(f"Execution time: {_linear_end - _linear_start} seconds")


print("--------- Binary search ---------")

low = 0
high = len(lst)-1

_bin_iter_count = 0

_bin_start = time.time()

while low <= high:
    mid = (low + high) // 2
    guess = lst[mid]
    _bin_iter_count += 1
    print("Iteration count:", _bin_iter_count)
    print(f"Low: {low}, High: {high}, MId: {mid}")
    if guess == item:
        print("Guess is", guess)
        break
    elif guess > item:
        high = mid - 1
    else:
        low = mid + 1
        
_bin_end = time.time()
print(f"Iterations count: {_bin_iter_count}")
print(f"Execution time: {_bin_end - _bin_start} seconds")



print("--------- Binary search in recursion (less optimal) ---------")

def mysearch(array, num, depth):
    print(array)
    arr_len = len(array)
    mid = arr_len // 2
    depth += 1
    if num == array[mid]:
        return True, depth
    elif num > array[mid]:
        return mysearch(array[mid+1:arr_len], num, depth)
    else:
        return mysearch(array[0:mid], num, depth)

search_list = list(range(100))
output = mysearch(search_list, 3, 0)
print(output)
