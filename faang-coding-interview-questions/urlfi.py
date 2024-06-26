def urlify_1(s: str, true_length: int) -> str:
  spaces = sum(1 for i in range(true_length) if s[i] == ' ')
  index = true_length + spaces * 2
  string_list = list(s)
  
  for i in range(true_length - 1, -1, -1):
    if string_list[i] == ' ':
      string_list[index - 3:index] = '%20'
      index -= 3
    else:
      string_list[index - 1] = string_list[i]
      index -= 1
    print(string_list)
  return ''.join(string_list)
  

def urlify_2(s: str) -> str:
  result = '%20'.join(s.rstrip().split(' '))
  return result
  
  
print(urlify_1('Mr John Smith    ', 13))
print(urlify_2('Mr John Smith    '))
  