class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map={
            'I' : 1,'V' : 5,'X':10,
            'L':50,'C':100,
            'D':500,'M':1000
        }
        total = 0
        prev = 0
        for ch in reversed(s):
            current = roman_map[ch]
            if current < prev:
                total -= current
            else:
                total += current
            prev = current
        return total        