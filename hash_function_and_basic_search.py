#Hash function and Basic search 
#Hash table O(1) 
def hash_search(hash_table, key):
    return hash_table.get(key, None)

#Basic search O(n)
def basic_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1