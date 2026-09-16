class Solution(object):
    def intersection(self, arr1, arr2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if arr1[i] == arr2[j] and arr1[i] not in result:
                    result.append(arr1[i])
        return result