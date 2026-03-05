from Binary_and_basic_search import binary_search, basic_search
from Selection_search_and_Sorting_algorithm import sellection_search, merge_sort
from hash_function_and_basic_search import hash_search, basic_search

import random
import string
import timeit

# Увеличим количество слов для более наглядной разницы в будущем
# 1000 слов — это очень мало для современных процессоров, разница будет в микросекундах.
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
        
        # Замер Binary Search (выполняем 1000 раз для точности)
        t_binary = timeit.timeit(lambda: binary_search(sorted_words, target), number=1000)
        index_binary = binary_search(sorted_words, target)
        print(f"Binary Search: Found at {index_binary} | Time (1000 runs): {t_binary:.6f}s")
        
        # Замер Basic Search
        t_basic = timeit.timeit(lambda: basic_search(words, target), number=1000)
        index_basic = basic_search(words, target)
        print(f"Basic Search: Found at {index_basic} | Time (1000 runs): {t_basic:.6f}s")

    elif answer == 2:
        # Для сортировки 1000 элементов сделаем меньше повторений (например, 10), 
        # так как Selection Sort довольно медленный (O(n^2)).
        
        t_selection = timeit.timeit(lambda: sellection_search(words.copy()), number=10)
        print(f"Selection Sort Time (10 runs): {t_selection:.6f}s")
        
        t_merge = timeit.timeit(lambda: merge_sort(words.copy()), number=10)
        print(f"Merge Sort Time (10 runs): {t_merge:.6f}s")
        
        print("\nNote: Selection Sort is O(n²), Merge Sort is O(n log n).")

    elif answer == 3:
        hash_table = {word: index for index, word in enumerate(words)}
        target = input("Enter a word to search: ")
        
        # Замер Hash Search (O(1))
        t_hash = timeit.timeit(lambda: hash_search(hash_table, target), number=1000)
        result_hash = hash_search(hash_table, target)
        print(f"Hash Search: Found at {result_hash} | Time (1000 runs): {t_hash:.6f}s")
        
        # Замер Basic Search (O(n))
        t_basic = timeit.timeit(lambda: basic_search(words, target), number=1000)
        index_basic = basic_search(words, target)
        print(f"Basic Search: Found at {index_basic} | Time (1000 runs): {t_basic:.6f}s")

    else:
        print("Invalid command.")