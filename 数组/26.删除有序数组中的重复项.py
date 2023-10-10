#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 如果nums为空列表，则直接返回0
        if len(nums) == 0:
            return 0
        
        slow = 0  # 慢指针
        for fast in range(len(nums)):  # 快指针遍历整个列表
            if nums[fast] != nums[slow]:  # 当快指针指向的元素与慢指针指向的元素不相等时
                slow += 1  # 慢指针向前移动一步
                nums[slow] = nums[fast]  # 更新慢指针指向的元素为快指针指向的元素
            fast += 1  # 快指针向前移动一步
        
        return slow + 1  # 返回去重后的列表长度
# @lc code=end

