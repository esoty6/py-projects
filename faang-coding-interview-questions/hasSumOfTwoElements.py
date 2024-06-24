def hasSumOfTwoElements(nums):
    num_set = set()
    
    for num in nums:
        for other_num in num_set:
            sum = num + other_num
            if sum in num_set:
                return True
            
        num_set.add(num)
    return False


nums: list[int] = [1,7,17,15]

print(hasSumOfTwoElements(nums))

nums: list[int] = [3,2,4,8,6]

print(hasSumOfTwoElements(nums))

nums: list[int] = [3,2,1]

print(hasSumOfTwoElements(nums))
