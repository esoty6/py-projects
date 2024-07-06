# O(1)
def check_length(func):
  def wrapper(first: str, second: str) -> bool:
    if len(first) != len(second):
      return False
    return func(first, second)
  return wrapper


# O(nlogn)
@check_length
def check_permutation_1(first: str, second: str) -> bool:
  # sorting two lists is O(2(nlogn)) -> O(nlogn)
  return sorted(first) == sorted(second)


# O(n)
@check_length
def check_permutation_2(first: str, second: str) -> bool:

  # Space complexity O(2n) -> O(n)
  frequency_first = [0] * 26
  frequency_second = [0] * 26
  
  # Time complexity O(n)
  # iterates over two different sources but with the same length O(n + m) -> m == n -> O(2n) -> O(n)
  for c in first:
    frequency_first[ord(c) - ord('a')] += 1
  for c in second:
    frequency_second[ord(c) - ord('a')] += 1
    
  return frequency_first == frequency_second


for i in range(1, 3):
  print(f"check_permutation_{i}('abc', 'cab'): ", eval(f"check_permutation_{i}('abc', 'cab')"))
  print(f"check_permutation_{i}('abcfe', 'cabef'): ", eval(f"check_permutation_{i}('abcfe', 'cabef')"))
  print(f"check_permutation_{i}('adc', 'zad'): ", eval(f"check_permutation_{i}('adc', 'zad')"))
  