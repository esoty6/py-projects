from datetime import datetime
import random

from merge_sort import merge_sort
from quick_sort import quick_sort


RANDOM_NUMBERS = [random.randint(-10**9, 10**9) for _ in range(1, 801)] 


def func_wrapper(func, *args):
  time = datetime.now()
  func(*args)
  print(f"Elapsed time for {func.__name__}: {datetime.now() - time}")

func_wrapper(merge_sort, RANDOM_NUMBERS)
func_wrapper(quick_sort, RANDOM_NUMBERS)
