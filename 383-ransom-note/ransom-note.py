class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq_r = {}
        freq_m = {}

        for i in ransomNote:
            freq_r[i] = freq_r.get(i, 0) + 1

        for j in magazine:
            freq_m[j] = freq_m.get(j, 0) + 1

        for i in freq_r:
            if freq_r[i] > freq_m.get(i, 0):
                return False
                
        return True