# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
 
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

import random
import sys
import time


def twoSum(nums: list, target: int) -> str:
  num_dict: dict = dict()
  
  for i, num in enumerate(nums):
    num_dict[num] = i
    complement = target - num
    
    if complement in num_dict:
      return f"[{num_dict[complement]}, {i}] | value[{num_dict[complement]}] -> {nums[num_dict[complement]]} | value[{i}] -> {nums[i]} | target -> {target}"
      
      
  return 'No corresponding values in the given array'


nums: list[int] = [2,7,11,15]
target: int = 9

print(twoSum(nums, target))

nums: list[int] = [3,2,4]
target: int = 6

print(twoSum(nums, target))

nums: list[int] = [3,3]
target: int = 6

print(twoSum(nums, target))

  
if __name__ == '__main__':
  runs = 3

  if sys.argv[1:]:
    try:
      runs = int(sys.argv[1])
    except ValueError as e:
      print(f'Error: {e}')

  print(f"Run for {runs} times...")
  time.sleep(0.5)
  
  for i in range(1, runs + 1):
    nums: list[int] = [random.randint(-10**9, 10**9) for _ in range(2, 10**4+1, 1)]
    target: int = random.randint(-10**9, 10**9)
    result = twoSum(nums=nums, target=target)
    print(f"Run No. {i}: {result}")
