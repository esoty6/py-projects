# without data structures # O(n^2)
def is_unique_1(word: str) -> bool:
  word_len = len(word)
  for i in range(word_len - 1):
    for j in range(i + 1, word_len):
      if word[i] == word[j]:
        return False
  return True
  
  
# without data structures
# with sort # O(nlogn)
def is_unique_1_1(word: str) -> bool:
  sorted_chars = sorted(word)
  sorted_chars_size = len(sorted_chars)
  for i in range(sorted_chars_size - 1):
    if sorted_chars[i] == sorted_chars[i + 1]:
      return False
  return True
  
  
# using set # O(n)
def is_unique_2(word: str) -> bool:
  char_set = set()
  for c in word:
    if c in char_set:
      return False
    else:
      char_set.add(c)
  return True 
  
  
if __name__ == '__main__':
  import sys
  
  if sys.argv[1::]:
    print(is_unique_1(sys.argv[1]))
    print(is_unique_1_1(sys.argv[1]))
    print(is_unique_2(sys.argv[1]))

  else:
    print('car', is_unique_1('car'))
    print('banana', is_unique_1('banana'))
    print('car', is_unique_1_1('car'))
    print('banana', is_unique_1_1('banana'))
    print('car', is_unique_2('car'))
    print('banana', is_unique_2('banana'))
  