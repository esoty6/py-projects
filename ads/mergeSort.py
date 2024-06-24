def merge(array, left, middle, right):
  sizeLeft = middle - left + 1
  sizeRight = right - middle
  
  LEFT_ARRAY = [0] * sizeLeft
  RIGHT_ARRAY = [0] * sizeRight
  
  for i in range(0, sizeLeft):
    LEFT_ARRAY[i] = array[left + i]

  for j in range(0, sizeRight):
    RIGHT_ARRAY[j] = array[middle + 1 + j]
      
  i = 0
  j = 0
  k = left
 
  while i < sizeLeft and j < sizeRight:
    if LEFT_ARRAY[i] <= RIGHT_ARRAY[j]:
      array[k] = LEFT_ARRAY[i]
      i += 1
    else:
      array[k] = RIGHT_ARRAY[j]
      j += 1
    k += 1

  while i < sizeLeft:
    array[k] = LEFT_ARRAY[i]
    i += 1
    k += 1
    
  while j < sizeRight:
    array[k] = RIGHT_ARRAY[j]
    j += 1
    k += 1
    
def sort(array, left, right):
  if left < right:
    middle = left + (right - left) // 2
    sort(array, left, middle)
    sort(array, middle + 1, right)
    merge(array, left, middle, right)

def mergeSort(array: list[int]) -> list[int]:
  sort(array, 0, len(array)-1)
  
  return array
  