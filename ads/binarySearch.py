import time
from datetime import datetime


class TargetValueError(Exception):
  pass


def ArgToInt(arg: str) -> int: 
  try:
    result = int(arg);
    
    if result < 0:
      raise TargetValueError("Value can't be lower than 0")

  except ValueError:
    print("Value has to be a positive integer")
    exit()
  except TargetValueError as tve:
    print(tve)
    exit()
    
  return result 
  
  
def checkTargetRange(arg: str) -> list[int]: 
  import random
  return random.sample(range(0, arg + 1), arg + 1)


def printResult(target: int, guess: int, time: time) -> None:
  endTime = datetime.now()
  print(f"Your value: {target}, guessed: {guess}. Time: {endTime - time}")
  exit()


if __name__ == '__main__':
  import sys
  
  startTime = datetime.now()
  
  targetValue = ArgToInt(sys.argv[1])
  targetRange = ArgToInt(sys.argv[2])

  sortedRange = list(range(0, targetRange + 1) )
  
  left = 0
  right = targetRange - 1
  guessIndex = left + (right-left) // 2
  guessValue = sortedRange[guessIndex]
  
  if guessValue == targetValue:
    printResult(target=targetValue, guess=guessValue, time=startTime)
  elif sortedRange[left] == targetValue:
    printResult(target=targetValue, guess=sortedRange[left], time=startTime)
  elif sortedRange[right] == targetValue:
    printResult(target=targetValue, guess=sortedRange[right], time=startTime)
    
  while targetValue != guessValue:
    if guessValue < targetValue:
      left = guessIndex
    elif guessValue > targetValue:
      right = guessIndex
      
    guessIndex = left + (right-left) // 2
    guessValue = sortedRange[guessIndex]

  printResult(target=targetValue, guess=guessValue, time=startTime)
  