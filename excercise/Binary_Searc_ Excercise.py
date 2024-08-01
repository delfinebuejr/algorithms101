def binary_search(arr, low, high, x):
  
  if high >= low:

    mid = (low+high) // 2

    if x == arr[mid]:
      return mid
    
    elif x > mid:
      return binary_search(arr, mid + 1, high, x)

    else:
      return binary_search(arr, 0, mid -1, x)
    
  else:
    return -1
  

data = [1,2,3,4,5,6,7,11,12,23,54,67]
x = 500

result = binary_search(data, 0, len(data) -1, x)

if result != -1:
  print("element found at: ", str(result))
else:
  print("element not found!")