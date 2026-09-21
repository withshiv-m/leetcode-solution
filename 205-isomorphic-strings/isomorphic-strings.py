class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s = {}
        map_t = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            # Check s -> t mapping
            if a in map_s and map_s[a] != b:
                return False

            # Check t -> s mapping
            if b in map_t and map_t[b] != a:
                return False

            map_s[a] = b
            map_t[b] = a

        return True