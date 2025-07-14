# using quick sort
# Time complexity: O(n log n) in average case, O(n²) in worst case.
# Space complexity: O(log n) for recursive stack.
def quicksort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start < end:
        partition_pos = partition(arr, start, end)
        quicksort(arr, start, partition_pos - 1)
        quicksort(arr, partition_pos + 1, end)

    return arr

def partition(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    l = start
    r = end - 1
    pivot = arr[end]

    while l < r:
        if arr[l] < pivot:
            l += 1
        elif arr[r] > pivot:
            r -= 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
    if arr[l] > pivot:
        arr[l], arr[end] = arr[end], arr[l]
        return l
    else:
        return end

# arr = [2,3,4,1,6,9,7,8,0]
arr = [6, 5, 4, 3, 2, 1, 0]
print(quicksort(arr))

# using merge sort
# Time complexity: O(n log n)
# Space complexity: O(n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # recursion
    left_sorted, right_sorted = merge_sort(left_arr), merge_sort(right_arr)

    # merge together
    sorted_arr = merge(left_sorted, right_sorted)

    return sorted_arr

def merge(arr1, arr2):
    merged = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

        # add remaining numbers if any
        arr1_tail = arr1[i:]
        arr2_tail = arr2[j:]

    return merged + arr1_tail + arr2_tail

# arr = [2,3,4,1,6,9,7,8,0]
arr = [6, 5, 4, 3, 2, 1, 0]
print(merge_sort(arr))
