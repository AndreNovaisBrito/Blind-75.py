from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


solution = Solution()

# Test the twoSum method
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]
