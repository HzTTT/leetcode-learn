#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0  # 初始化慢指针和快指针，分别指向数组的开头
        while fast < len(nums):  # 当快指针小于数组长度时循环
            if nums[fast] != 0:  # 如果快指针指向的元素不为0
                nums[slow] = nums[fast]  # 将快指针指向的元素赋值给慢指针指向的位置
                slow += 1  # 慢指针向后移动一位
            fast += 1  # 快指针向后移动一位
        while slow < len(nums):  # 当慢指针小于数组长度时循环
            nums[slow] = 0  # 将慢指针指向的位置赋值为0
            slow += 1  # 慢指针向后移动一位
    
# @lc code=end
