class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = min(nums)
        largest = max(nums)

        while largest != 0:
            smallest,largest = largest,smallest%largest
        return smallest