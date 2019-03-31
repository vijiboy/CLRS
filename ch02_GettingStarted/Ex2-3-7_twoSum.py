def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :return: indices of two numbers whose sum is target
    """
    diff = {}
    for i in range(len(nums)): 
        if diff.has_key(nums[i]):
            return [diff[nums[i]], i]
        diff[target-nums[i]] = i # save diff and its index 
    return [] # No sum found

assert [1,4] == twoSum([11,2,13,7,8], 10)
assert [2,4] == twoSum([-1,-2,-3,-4,-5], -8)
