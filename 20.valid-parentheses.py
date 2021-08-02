#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": 1, ")": -1, "{": 2, "}": -2, "[": 3, "]": -3, }
        flag = 0
        for i in range(len(s)):
            flag += dic[s[i]]
            if flag < 0:
                return False
        return True


# @lc code=end
