# LABSHEET 7 - PROBLEM 1
# Heap, Priority Queue and Heap Sort


import heapq


# -------------------------------
# MIN HEAP
# -------------------------------

min_heap = []

for value in [40, 20, 30, 10, 50]:
    heapq.heappush(min_heap, value)

print("Min Heap:", min_heap)

print("Removing elements from Min Heap:")

while min_heap:
    print(heapq.heappop(min_heap), end=" ")


# -------------------------------
# MAX HEAP
# -------------------------------

max_heap = []

for value in [40, 20, 30, 10, 50]:
    heapq.heappush(max_heap, -value)

print("\n\nMax Heap:")

temp = max_heap.copy()

while temp:
    print(-heapq.heappop(temp), end=" ")


# -------------------------------
# PRIORITY QUEUE
# -------------------------------

print("\n\nPriority Queue:")

priority_queue = []

heapq.heappush(priority_queue, (2, "Task B"))
heapq.heappush(priority_queue, (1, "Task A"))
heapq.heappush(priority_queue, (3, "Task C"))

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print("Priority:", priority, "Task:", task)


# -------------------------------
# HEAP SORT
# -------------------------------

def heap_sort(arr):

    heap = arr.copy()

    heapq.heapify(heap)

    sorted_array = []

    while heap:
        sorted_array.append(heapq.heappop(heap))

    return sorted_array


arr = [40, 10, 30, 50, 20]

print("\nOriginal Array:", arr)

sorted_array = heap_sort(arr)

print("Heap Sorted Array:", sorted_array)

# LABSHEET 7 - PROBLEM 2
# Rearrange Array to Maximize Adjacent Sum Difference


def maximize_difference(arr):

    arr.sort()

    n = len(arr)

    result = []

    left = 0
    right = n - 1

    # Take smallest, largest, second smallest,
    # second largest, and so on
    while left <= right:

        if left == right:
            result.append(arr[left])
            break

        result.append(arr[left])
        result.append(arr[right])

        left += 1
        right -= 1

    # Calculate total adjacent difference
    total = 0

    for i in range(1, n):
        total += abs(result[i] - result[i - 1])

    return result, total


# Main program

arr = list(map(int, input("Enter array elements: ").split()))

result, total = maximize_difference(arr)

print("Rearranged Array:", result)
print("Maximum Sum of Absolute Differences:", total)

# LABSHEET 7 - PROBLEM 3
# Smallest Subarray with Sum Greater Than Target
# Using Sliding Window


def smallest_subarray(arr, target):

    left = 0
    current_sum = 0

    min_length = float('inf')

    for right in range(len(arr)):

        # Add current element
        current_sum += arr[right]

        # Shrink window while sum is greater than target
        while current_sum > target:

            window_length = right - left + 1

            min_length = min(min_length, window_length)

            current_sum -= arr[left]

            left += 1

    # If no valid subarray was found
    if min_length == float('inf'):
        return -1

    return min_length


# Main program

arr = list(map(int, input("Enter array elements: ").split()))

target = int(input("Enter target: "))

result = smallest_subarray(arr, target)

print("Smallest Subarray Length:", result)
