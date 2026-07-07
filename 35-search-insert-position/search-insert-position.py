class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (begin+end)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                begin = mid + 1
        else:
            return begin