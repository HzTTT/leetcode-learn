#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 如果nums为空列表，则直接返回0
        if len(nums) == 0:
            return 0
        
        # 定义慢指针slow初始位置为0
        slow = 0
        
        # 使用快指针fast遍历nums列表
        for fast in range(len(nums)):
            # 如果当前元素不等于目标值val
            if nums[fast] != val:
                # 将当前元素赋值给慢指针所指向的位置
                nums[slow] = nums[fast]
                # 慢指针向后移动一位
                slow += 1
        
        # 返回慢指针的位置，即新列表的长度
        return slow
            
                
# @lc code=end
