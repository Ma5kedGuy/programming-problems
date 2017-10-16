# Python program for implementation of Bubble Sort
 # Static input
 
 # Function to do Bubble sort
 # Traverse through 1 to len(arr)
 # Swap consecutive elements of arr[0..i-1], that are
 # greater than the elements to the immediate right
 # of their current position
def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[i]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
 
arr = [10, 20, 7, 80, 32, 78]
bubble_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("{0:d}".format(arr[i]))
