
def partition(arr):
  left = []
  right = []
  pivot = arr[0]

  # iterate over the rest of the array 
  for num in arr[1:]:
  # if the element is greater than the pivot, in the right
    if num > pivot:
      right.append(num)
  # else, in the left
    else:
      left.append(num)
  return left, pivot, right

def quicksort(arr):
  if len(arr) == 0:
    return arr

  # partition here into left, pivot and right
  # divide
  left, pivot, right = partition(arr)

  return quicksort(left) + pivot + quicksort(right)

def quicksort_in_place(arr):
  pass

  # quicksort(0, pivot_index) + pivot + quicksort(pivot_index + 1, len(arr))

num = [4,6,5,2,1,9,8,7,0]

print(quicksort(num))
