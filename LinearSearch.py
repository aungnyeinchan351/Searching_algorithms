def LinearSearch(arr, SearchKey):
    for i in range(len(arr)):
        if arr[i] == SearchKey:
            return i
    return -1
array = [10, 20, 30, 40, 50]
value = 30
result = LinearSearch(array, value)
print("{} is found at index of {}".format(value, result))