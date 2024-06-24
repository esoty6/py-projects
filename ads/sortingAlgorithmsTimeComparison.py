from datetime import datetime
import random

from mergeSort import mergeSort
from quickSort import quickSort


RANDOM_NUMBERS = [random.randint(-10**9, 10**9) for _ in range(1, 801)] 


def funcWrapper(func, *args):
  time = datetime.now()
  func(*args)
  print(f"Elapsed time for {func.__name__}: {datetime.now() - time}")

funcWrapper(mergeSort, RANDOM_NUMBERS)
funcWrapper(quickSort, RANDOM_NUMBERS)
