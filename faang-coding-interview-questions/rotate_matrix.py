def rotate_matrix(matrix: list) -> list:
  n = len(matrix)
  
  if n == 0 or len(matrix[0]) != n:
    return matrix
  
  for layer in range(n // 2):
    first = layer
    last = n - 1 - layer
    
    for i in range(first, last):
      offset = i - first
      
      # save top value
      temp = matrix[first][i]
      
      # left -> top
      matrix[first][i] = matrix[last - offset][first]

      # bottom -> left
      matrix[last - offset][first] = matrix[last][last - offset]
      
      # right -> bottom
      matrix[last][last - offset] = matrix[i][last]

      # saved top -> right
      matrix[i][last] = temp
      
  return matrix


def print_matrix(matrix: list) -> None:
  for row in matrix:
    print(row) 
  
  
initial_matrix = [[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]]

print_matrix(initial_matrix)
print_matrix(rotate_matrix(initial_matrix))
  