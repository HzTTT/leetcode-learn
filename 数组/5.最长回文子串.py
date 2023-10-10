#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def palindrome(self, s: str, l: int, r: int) -> str:
        # 从中心向外扩展子串，直到不再是回文串为止
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # 遍历字符串中的每个字符
        for i in range(len(s)):
            # 检查奇数长度的回文串
            res1 = self.palindrome(s, i, i)
            # 检查偶数长度的回文串
            res2 = self.palindrome(s, i, i+1)
            # 更新目前找到的最长回文串
            res = max(res1, res, key=len)
            res = max(res2, res, key=len)
        return res

        
# @lc code=end

