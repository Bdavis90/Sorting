# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i, value in enumerate(arr):
    if value == target:
      return i
  
  # TO-DO: add missing code

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while low <= high:
    # go to middle
    middle = (low + high)//2
    # ask if the middle is less than or greater than our target
    # if less, elminate the right-hand side
    if target < arr[middle]:
      high = middle - 1
    # if greater, elminate the left-hand side 
    elif target > arr[middle]:
      low = middle + 1
    # if neither target is the middle
    else:
      return middle

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
