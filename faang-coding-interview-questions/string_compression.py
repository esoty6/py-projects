# O(n)
def string_compression(s: str) -> str:
  if not s:
    return s
  
  compressed = list()
  compressed_length = 0
  count = 1
  
  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      count += 1
    else:
      compressed_part = f'{s[i - 1]}{count}'
      compressed.append(compressed_part)
      compressed_length += len(compressed_part)
      count = 1
      
    if compressed_length >= len(s):
      return s
  
  compressed_part = f'{s[-1]}{count}'
  compressed.append(compressed_part)
  compressed_length += len(compressed_part)
  
  return ''.join(compressed) if compressed_length < len(s) else s
  
  
print(string_compression('Aaabbbccaaa'))  
print(string_compression('aaabbbcccca'))  
print(string_compression('abcaccdee'))
  