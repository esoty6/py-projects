import random

from execution_time import execution_time
from merge_sort import merge_sort
from quick_sort import quick_sort


RANDOM_NUMBERS = [random.randint(-10**9, 10**9) for _ in range(1, 801)] 


execution_time(merge_sort, RANDOM_NUMBERS)
execution_time(quick_sort, RANDOM_NUMBERS)
