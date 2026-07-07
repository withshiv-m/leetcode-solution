class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        start =strs[0]
        ans = ""
        for i in range(len(start)):
            for word in strs:
                if i >= len(word) or word[i] != start[i]:
                    return ans
            ans += start[i]
        return ans