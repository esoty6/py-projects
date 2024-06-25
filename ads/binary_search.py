import time
from datetime import datetime


class TargetValueError(Exception):
  pass

def arg_to_int(arg: str) -> int: 
  try:
    result = int(arg)
    
    if result < 0:
      raise TargetValueError("Value can't be lower than 0")

  except ValueError:
    print("Value has to be a positive integer")
    exit()
  except TargetValueError as tve:
    print(tve)
    exit()
    
  return result 
  
  
def check_target_range(arg: str) -> list[int]: 
  import random
  return random.sample(range(0, arg + 1), arg + 1)


def print_result(target: int, guess: int, time: time) -> None:
  end_time = datetime.now()
  print(f"Your value: {target}, guessed: {guess}. Time: {end_time - time}")
  exit()


if __name__ == '__main__':
  import sys
  
  start_time = datetime.now()
  
  target_value = arg_to_int(sys.argv[1])
  target_range = arg_to_int(sys.argv[2])

  sorted_range = list(range(0, target_range + 1) )
  
  left = 0
  right = target_range - 1
  guess_index = left + (right-left) // 2
  guess_value = sorted_range[guess_index]
  
  if guess_value == target_value:
    print_result(target_value, guess_index, start_time)
  elif sorted_range[left] == target_value:
    print_result(target_value, sorted_range[left], start_time)
  elif sorted_range[right] == target_value:
    print_result(target_value, sorted_range[right], start_time)
    
  while target_value != guess_value:
    if guess_value < target_value:
      left = guess_index
    elif guess_value > target_value:
      right = guess_index
      
    guess_index = left + (right - left) // 2
    guess_value = sorted_range[guess_index]

  print_result(target_value, guess_value, start_time)
  