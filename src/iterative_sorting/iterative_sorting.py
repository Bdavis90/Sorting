# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        
        # TO-DO: swap
    return arr

nums = [2,6,8,9,1,0,5]
print(selection_sort(nums))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort(nums))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return arr

    if maximum == -1:
        maximum = max(arr)

    count = [0] * (maximum + 1)

    for value in arr:
        if value < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        count[value] += 1

    j = 0

    for i in range(len(count)):
        while count[i] > 0:
            arr[j] = i
            count[i] -= 1
    return arr

    