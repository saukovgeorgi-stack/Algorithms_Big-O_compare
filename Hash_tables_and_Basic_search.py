def hash_table():
    hash_table = {}
    
    hash_table['name'] = 'Alice'
    hash_table['age'] = 30
    hash_table['city'] = 'New York'
    
    # Accessing values using keys
    print(hash_table['name'])  # Output: Alice
    print(hash_table['age'])   # Output: 30
    print(hash_table['city'])  # Output: New York
    
    if 'name' in hash_table:
        print("Key 'name' exists in the hash table.")
    
    del hash_table['age']
    
    if 'age' not in hash_table:

        print("Key 'age' has been removed from the hash table.")
