class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)

        # special cases where the max of one list is smaller than the min of the other list (the code below doesn't work in these cases)
        if nums1[len(nums1) - 1] < nums2[0]:
            pass

        min1 = 0
        max1 = len(nums1) - 1
        ind1 = (min1 + max1) // 2
        min2 = 0
        max2 = len(nums2) - 1
        ind2 = (min2 + max2) // 2

        while ind1 + ind2 != (total_len - 1) // 2:
            if nums1[ind1] < nums2[ind2]:
                if ind1 + ind2 < (total_len - 1) // 2:
                    min1 = ind1 + 1
                else:
                    max2 = ind2 - 1
            else:
                if ind1 + ind2 < (total_len - 1) // 2:
                    min2 = ind2 + 1
                else:
                    max1 = ind1 - 1

            ind1 = (min1 + max1) // 2
            ind2 = (min2 + max2) // 2
            print(str(min1) + ' ' + str(max1) + ' ' + str(min2) + ' ' + str(max2))

        if total_len % 2 == 1:
            return min(nums1[ind1], nums2[ind2])

if __name__ == '__main__':
    sol = Solution()
    nums2 = [0,1,2,3,4,14]
    nums1 = [5,6,7,8,9,10,11,12,13]
    print('answer = ' + str(sol.findMedianSortedArrays(nums1, nums2)))
