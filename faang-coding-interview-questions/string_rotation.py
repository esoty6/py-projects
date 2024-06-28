def is_rotation(s1: str, s2: str) -> bool:
  if len(s1) != len(s2) or len(s1) == 0:
    return False
    
  s1s1 = s1 + s1
    
  return is_substring(s1s1, s2)

def is_substring(string: str, substring: str) -> bool:
  return substring in string


print(is_rotation('waterbottle', 'erbottlewat')) 
print(is_rotation('potato', 'topota'))            
print(is_rotation('tomato', 'tomtoa'))         
  