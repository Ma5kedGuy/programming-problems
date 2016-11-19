def merge_sort(data, start, end):
    # [start, end)
    if start >= end - 1 :
        return
    mid = (start + end)/2
    merge_sort(data, start, mid)
    merge_sort(data, mid, end)

    i = 0
    j = 0
    index = start
    
    left = data[start: mid]
    right = data[mid : end]

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[index] = left[i]
            i += 1
        else:
            data[index] = right[j]
            j += 1
        index += 1
    while i < len(left) :
        data[index] = left[i]
        i += 1
        index += 1
    while j < len(right):
        data[index] = right[j]
        j += 1
        index +=1

# test
if __name__ == '__main__':
    test_input = []
    merge_sort(test_input, 0, len(test_input))
    assert(test_input) == []
    
    test_input = [1]
    merge_sort(test_input, 0, len(test_input))
    assert(test_input) == [1]
    
    test_input = [3,2,1]
    merge_sort(test_input, 0, len(test_input))
    assert(test_input) == [1,2,3]
    
    test_input = [4,3,2,1]
    merge_sort(test_input, 0, len(test_input))
    assert(test_input) == [1,2,3,4]

    test_input = [5,2,5,5,5,6,8,8,8,7,1,3,2,9]
    merge_sort(test_input, 0, len(test_input))
    assert(test_input) == [1, 2, 2, 3, 5, 5, 5, 5, 6, 7, 8, 8, 8, 9]

