class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_s = {}
        freq_t = {}
        if len(s) == len(t):
            for i in s:
                freq_s[i] = freq_s.get(i,0)+1
            for j in t:
                freq_t[j] = freq_t.get(j,0)+1
            if freq_s == freq_t:
                return True
            else:
                return False
        else:
            return False