#Hash tables and Basic search 
#Hash table O(1) 
def hash_table():
    hash_table = {}
    
    # Adding key-value pairs to the hash table
    hash_table['name'] = 'Alice'
    hash_table['age'] = 30
    hash_table['city'] = 'New York'
    
    # Accessing values using keys
    print(hash_table['name'])  # Output: Alice
    print(hash_table['age'])   # Output: 30
    print(hash_table['city'])  # Output: New York
    
    # Checking if a key exists in the hash table
    if 'name' in hash_table:
        print("Key 'name' exists in the hash table.")
    
    # Removing a key-value pair from the hash table
    del hash_table['age']
    
    # Checking if a key exists after deletion
    if 'age' not in hash_table:
        print("Key 'age' has been removed from the hash table.")