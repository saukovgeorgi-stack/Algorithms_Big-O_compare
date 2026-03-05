#In this file we will compare searching in sorted list using binary search and basic search
#Binary search Big-O: O(Log(n))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

#Basic search Big-O: O(n)

def basic_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1