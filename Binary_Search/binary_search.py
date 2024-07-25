## returns the index of x in an array if present else -1
def binary_search(arr, low, high, x):
  
  # check if the target is within the given range of data
  if arr[high] >= arr[low]:

    # get the mid element "index" using floor division 
    # to be able to handle arrays with odd number of elements
    mid = (low + high) // 2

    # return the mid element "index" if it matches "x"
    if x == arr[mid]:
      return mid

    # ignore left sub-array if "x" is greater than mid element
    elif x > arr[mid]:
      return binary_search(arr, mid + 1, high, x)

    # ignore right sub-array if x is less than mid element
    else:
      return binary_search(arr, low, mid - 1, x)

  else:
    #element is not present in the array
    return -1


# test array data
# data should be arranged in ascending order
arr = [1, 2, 3, 4, 5, 6, 7]
x = 5

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
  print("element is present in index: ", str(result))
else:
  print("element is not present in the array.")
