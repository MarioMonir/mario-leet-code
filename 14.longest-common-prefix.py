#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)[::-1]
        if len(strs) < 2:
            return strs[0] if len(strs) == 1 else ""
        lead = strs[0]
        count = len(lead)
        if count == 0:
            return ""
        for i in range(1,len(strs)):
            match = 0
            for j in range(len(strs[i])):
                word = strs[i]
                if word[j] == lead[j]:
                    match += 1
                else:
                    break
            if match == 0:
                return ""
            else:
                count = match if match < count else count
        return lead[:count]
        
# @lc code=end

