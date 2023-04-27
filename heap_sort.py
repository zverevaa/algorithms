
num_arr = [11, 5, 2, 13, 6, 1]


def heapify(arr, heap_size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and arr[largest] < arr[left]:
        largest = left
    if right < heap_size and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, heap_size, largest)


def heap_sort(arr):
    heap_size = len(arr)

    for i in range(heap_size//2 - 1, -1, -1):
        heapify(arr, heap_size, i)

    for i in range(heap_size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


print("Unsorted array:")
for i in range(len(num_arr)):
    print("%d" % num_arr[i], end=" ")

heap_sort(num_arr)

print("\nSorted array:")
for i in range(len(num_arr)):
    print("%d" % num_arr[i], end=" ")
