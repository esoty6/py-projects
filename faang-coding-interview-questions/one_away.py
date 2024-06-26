# O(min(n, m)) -> so basically O(n)
# in the worst case, func will traverse the entire shorter string
def one_away(s1: str, s2: str) -> bool:
  if abs(len(s1) - len(s2)) > 1:
    return False
  
  longer_string, shorter_string = (s1, s2) if len(s1) >= len(s2) else (s2, s1)
  differences = 0
  are_the_same_length = len(s1) == len(s2)
  i, j = 0, 0
  
  while i < len(shorter_string) and j < len(longer_string):
    if shorter_string[i] != longer_string[j]:
      differences += 1
      if differences > 1:
        return False
      if are_the_same_length:
        i += 1
    else:
      i += 1
    j += 1

  return True
  
  
print(one_away('pale', 'ple'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'pales'))
print(one_away('aple', 'pale'))
print(one_away('pales', 'palelse'))
