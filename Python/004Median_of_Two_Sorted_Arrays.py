#coding:utf-8
'''
python sort函数应该是O(nlogn)
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        add_num=nums1+nums2
        add_num.sort()
        if len(add_num)%2:
            return add_num[len(add_num)/2]
        else:
            return ( add_num[len(add_num)/2-1] + add_num[len(add_num)/2])/2.0

if __name__ == '__main__':
    s=Solution()
    nums1=[1,2]
    nums2=[3,4]
    print s.findMedianSortedArrays(nums1,nums2)
