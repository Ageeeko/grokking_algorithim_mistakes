#page 9
def binary_search(list1, item):
    start = 0
    end = len(list1) - 1
    while start - end < -1:
        mid = round((end + start)/2)
        if list1[mid] == item:
            return mid
        elif l1[mid] > item:
            end = mid
        else:
            start = mid
    return None
    
l1 = [i for i in range(1, 21)]
guess = 11
index = binary_search(l1, 30)
print(index)
