#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
from typing import List
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 初始化左右指针
        left, right = 0, len(s) - 1
        
        # 当左指针小于右指针时循环执行
        while left < right:
            # 交换左右指针对应的元素
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            
            # 更新左右指针的位置
            left += 1
            right -= 1
# @lc code=end
