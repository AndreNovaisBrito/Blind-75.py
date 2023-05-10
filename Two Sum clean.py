def twoSum(nums, target):
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return


# Test the twoSum method
result = twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]
