import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
            print(ans)
        return ans.values()

solution = Solution()
solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])