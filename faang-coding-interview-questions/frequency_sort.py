from collections import Counter
from functools import partial
import random


def sort_order(item, count):
  return (count[item], item)


def items_sort(items):
    count = Counter(items)
    return sorted(items, key=partial(sort_order, count=count))


test1 = [3,3,1,2,2,2,4,5,5,5]
test2 = [3,1,2,2,2,4,3]
test3 = [random.randint(1, 10**2) for _ in range(1, 10**2 + 1, 1)]

print(items_sort(test1))
print(items_sort(test2))
print(items_sort(test3))
