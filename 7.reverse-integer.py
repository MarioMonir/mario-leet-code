#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x > 2147483647 or x < -2147483647:
            return 0
        if x >= 0:
            res = int(str(x)[::-1])
            return 0 if res > 2147483647 else res 
        else:
            res = int("-"+str(x)[:0:-1])
            return 0 if res < -2147483647 else res
# @lc code=end

