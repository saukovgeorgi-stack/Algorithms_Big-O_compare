from Binary_and_basic_search import binary_search, basic_search
from Selection_search_and_Sorting_algorithm import sellection_search, merge_sort
from hash_function_and_basic_search import hash_search, basic_search

import random
import string
import timeit
import math

words = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(1000)]

if len(words) == 1000:
    print("Generated 1000 random words successfully.")
    print("User commands:\n 1 - Binary and Basic search\n 2 - Selection and Merge sort\n 3 - Hash and Basic search")
    
    try:
        answer = int(input("Choose option: "))
    except ValueError:
        answer = 0
    if answer == 1:
        target = input("Enter a word to search: ")
        sorted_words = sorted(words)
        N = len(words)
    
        t_binary = timeit.timeit(lambda: binary_search(sorted_words, target), number=1000)
        t_basic = timeit.timeit(lambda: basic_search(words, target), number=1000)
    
        ratio = t_basic / t_binary
    
        ops_basic = N  # В худшем случае
        ops_binary = math.ceil(math.log2(N)) # log2(1000) ≈ 10
    
        print(f"\n--- Search Comparison ---")
        print(f"Basic Search (O(N)): ~{ops_basic} ops | Time: {t_basic:.6f}s")
        print(f"Binary Search (O(log N)): ~{ops_binary} ops | Time: {t_binary:.6f}s")
        print(f"RESULT: Binary Search is {ratio:.2f}x faster!")

    elif answer == 2:
        N = len(words)
    
        t_selection = timeit.timeit(lambda: sellection_search(words.copy()), number=10)
        t_merge = timeit.timeit(lambda: merge_sort(words.copy()), number=10)
    
        ratio = t_selection / t_merge
    
        ops_selection = N**2 # 1000^2 = 1,000,000
        ops_merge = int(N * math.log2(N)) # 1000 * 10 = 10,000
    
        print(f"\n--- Sorting Comparison ---")
        print(f"Selection Sort (O(N²)): ~{ops_selection:,} ops | Time: {t_selection:.6f}s")
        print(f"Merge Sort (O(N log N)): ~{ops_merge:,} ops | Time: {t_merge:.6f}s")
        print(f"RESULT: Merge Sort is {ratio:.2f}x faster!")

    elif answer == 3:
        hash_table = {word: index for index, word in enumerate(words)}
        target = input("Enter a word to search: ")
    
        t_hash = timeit.timeit(lambda: hash_search(hash_table, target), number=1000)
        t_basic = timeit.timeit(lambda: basic_search(words, target), number=1000)
    
        ratio = t_basic / t_hash
    
        print(f"\n--- Hash Comparison ---")
        print(f"Basic Search (O(N)): ~{len(words)} ops | Time: {t_basic:.6f}s")
        print(f"Hash Search (O(1)): ~1 op | Time: {t_hash:.6f}s")
        print(f"RESULT: Hash Search is {ratio:.2f}x faster!")