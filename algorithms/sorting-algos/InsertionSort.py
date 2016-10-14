# Python program for implementation of Insertion Sort
# Static input

# Function to do insertion sort
# Traverse through 1 to len(arr)
# Move elements of arr[0..i-1], that are
# greater than key, to one position ahead
# of their current position
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [10, 20, 7, 80, 32, 78]
insertion_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print "{0:d}".format(arr[i])
