def JumpSearch(list1, val):
    import math
    gap = math.sqrt(len(list1))
    left = 0
    while(list1[int(min(gap, len(list1))-1)]<val):
        left = gap
        gap = gap + math.sqrt(len(list1))
        if(left>=len(list1)):
            break
    while(list1[int(left)]<val):
        left =left + 1
        if(left== min(gap, len(list1))):
            break
    if(list1[int(left)]==val):
        return int(left)
arr = [1,2,6,7,8,10]
searchitem = 8
result = JumpSearch(arr,searchitem)
print("{} is found at index of {}".format(searchitem, result))