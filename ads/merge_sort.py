def merge(array, left, middle, right):
  size_left = middle - left + 1
  size_right = right - middle
  
  LEFT_ARRAY = [0] * size_left
  RIGHT_ARRAY = [0] * size_right
  
  for i in range(0, size_left):
    LEFT_ARRAY[i] = array[left + i]

  for j in range(0, size_right):
    RIGHT_ARRAY[j] = array[middle + 1 + j]
      
  i = 0
  j = 0
  k = left
 
  while i < size_left and j < size_right:
    if LEFT_ARRAY[i] <= RIGHT_ARRAY[j]:
      array[k] = LEFT_ARRAY[i]
      i += 1
    else:
      array[k] = RIGHT_ARRAY[j]
      j += 1
    k += 1

  while i < size_left:
    array[k] = LEFT_ARRAY[i]
    i += 1
    k += 1
    
  while j < size_right:
    array[k] = RIGHT_ARRAY[j]
    j += 1
    k += 1
    
def sort(array, left, right):
  if left < right:
    middle = left + (right - left) // 2
    sort(array, left, middle)
    sort(array, middle + 1, right)
    merge(array, left, middle, right)

def merge_sort(array: list[int]) -> list[int]:
  sort(array, 0, len(array)-1)
  
  return array
  