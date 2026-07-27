class Solution(object):
    def plusOne(self, digit):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digit)
        for i in range(n-1,-1,-1):
            if digit[i] < 9:
                digit[i] += 1
                return digit
            digit[i] = 0
        return [1] + digit
        