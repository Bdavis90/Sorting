# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    a = 0
    b = 0
    # iterate through the lengths of the arrays
    for i in range(elements):
    # if a counter is bigger or equal to arrA length
        if a >= len(arrA):
    #  add from arrB to the merged_arr
            merged_arr[i] = arrB[b]
            b += 1
            print(merged_arr, 'first merge')
    # if b counter is bigger than or equal to arrB length
        elif b >= len(arrB):
    # add from arrA to the merge_arr
            merged_arr[i] = arrA[a]
            a += 1
            print(merged_arr, 'second merge')
    # if element at arrA index is less than the one at arrB
        elif arrA[a] < arrB[b]:
    # add the lower arrA[a] to the merged_arr
            merged_arr[i] = arrA[a]
            a += 1
            print(merged_arr, 'arrA merge')
    # if element at arrB index is less than the one at arrB
        elif arrB[b] < arrA[a]:
    # add the lower arrB[b] to the merged_arr
            merged_arr[i] = arrB[b]
            b += 1
            print(merged_arr,'arrB merge')
    # TO-DO
    
    return merged_arr

num = [4,6,5,2,9,1]
num1 = [3,8,7,0,]

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    middle = len(arr)//2
    arr_right = arr[middle:]
    arr_left = arr[:middle]
    print(arr_left, 'left')
    print(arr_right, 'right')
    
    if len(arr) <= 1:
        return arr

    else:
        left = merge_sort(arr_left)
        print(arr_left,'merge_left')
        right = merge_sort(arr_right)
        print(arr_right, 'merge_right')
        arr = merge(left, right)
    # TO-DO

    return arr

print(merge_sort(merge(num, num1)))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr




# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
