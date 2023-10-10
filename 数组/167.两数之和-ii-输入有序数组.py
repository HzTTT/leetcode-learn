#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                # 题目要求的索引是从 1 开始的
                return [left + 1, right + 1]
            elif sum < target:
                left += 1 # 让 sum 大一点
            else:
                right -= 1 # 让 sum 小一点
        return [-1, -1]
        
# @lc code=end

