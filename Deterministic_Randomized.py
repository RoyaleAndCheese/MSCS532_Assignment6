## Deterministic Algorithm
def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Step 1: Divide into groups of five
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # Step 2: Recursively find the median of medians
    pivot = deterministic_select(medians, len(medians) // 2 + 1)

    # Step 3: Partition the array
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equals = [x for x in arr if x == pivot]

    # Step 4: Determine which part contains the k-th element
    if k <= len(low):
        return deterministic_select(low, k)
    elif k <= len(low) + len(equals):
        return pivot
    else:
        return deterministic_select(high, k - len(low) - len(equals))



#Randomized Algorithm
import random

def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Step 1: Randomly select a pivot
    pivot = random.choice(arr)

    # Step 2: Partition the array
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equals = [x for x in arr if x == pivot]

    # Step 3: Determine which part contains the k-th element
    if k <= len(low):
        return randomized_select(low, k)
    elif k <= len(low) + len(equals):
        return pivot
    else:
        return randomized_select(high, k - len(low) - len(equals))
    


#Testing
import time

def test_selection_algorithms():
    # Generate test cases
    random_array = [random.randint(1, 90000) for _ in range(90000)]
    sorted_array = sorted(random_array)
    reverse_sorted_array = sorted_array[::-1]
    
    # k-th element to find
    k = len(random_array) // 2

    # Test arrays
    test_cases = {
        "Random": random_array,
        "Sorted": sorted_array,
        "Reverse Sorted": reverse_sorted_array
    }

    for name, array in test_cases.items():
        print(f"\nTesting on {name} Array:")

        # Deterministic Selection
        start = time.time()
        result = deterministic_select(array, k)
        end = time.time()
        print(f"Deterministic Selection Result: {result}, Time: {end - start:.6f} seconds")

        # Randomized Selection
        start = time.time()
        result = randomized_select(array, k)
        end = time.time()
        print(f"Randomized Selection Result: {result}, Time: {end - start:.6f} seconds")

# Run the tests
test_selection_algorithms()
