def BinarySearch(arr, SearchKey):
    first = 0
    last = len(arr)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if arr[mid] == SearchKey:
            index = mid
        else:
            if SearchKey<arr[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
array = [10, 20, 30, 40, 50]
value = 30
result = BinarySearch(array, value)
print("{} is found at index of {}".format(value, result))
