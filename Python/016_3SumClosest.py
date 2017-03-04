class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret=['a','']
        nums.sort()
        print nums
        for i in xrange(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            gaps=['a','']
            while l<r:
                temp=nums[i]+nums[l]+nums[r]
                gap=temp-target if temp>target else target-temp
                if gap <= gaps[0]:
                    gaps[0]=gap
                    gaps[1]=temp
                print i,l,r,temp,gaps
                if temp >target:
                    r-=1
                elif temp < target:
                    l+=1
                else:
                    return target
            if gaps[0]<ret[0]:
                ret[0]=gaps[0]
                ret[1]=gaps[1]
            print "ret=",ret
        print ret
        return ret[1]
if __name__ == '__main__':
    example = Solution()
    nums=[-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
    target=0
    print example.threeSumClosest(nums,target)
