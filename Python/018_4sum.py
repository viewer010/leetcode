#coding=utf8
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret=[]
        nums.sort()
        print nums
        def threeSum(self, nums,target):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            ret=[]
            nums.sort()
            for i in xrange(0,len(nums)-2):
                if i>0 and nums[i-1] == nums[i]:
                    continue
                l,r=i+1,len(nums)-1
                while l<r:
                    s=nums[i]+nums[l]+nums[r]
                    if s<target:
                        l=l+1
                    elif s>target:
                        r=r-1
                    else:
                        ret.append([nums[i],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r=r-1
                        l=l+1
                        r=r-1
            return ret
        for i in xrange(0,len(nums)-3):
            if i>0 and nums[i-1] == nums[i]:
                continue
            rets=threeSum(self,nums[i+1:],target-nums[i])
            #print rets, nums[i],nums[i+1:]
            if rets:
                ret=ret+[ [nums[i]]+temp for temp in rets]
        return ret
if __name__ == '__main__':
    example = Solution()
    nums=[1, 0, -1, 0, -2, 2]
    target=0
    print example.fourSum(nums,target)
