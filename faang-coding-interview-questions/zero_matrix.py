# O(nm)
def zero_matrix(n: int, m:int) -> list | None:
  if n < 1 or m < 1:
    return None
  
  matrix = [[0 for _ in range(m)] for _ in range(n)]

  return matrix


print(zero_matrix(2,3))
print(zero_matrix(3,3))
print(zero_matrix(7,3))
  