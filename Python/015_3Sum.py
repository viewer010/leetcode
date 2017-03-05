class Solution(object):
    def threeSum(self, nums):
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
                if s<0:
                    l=l+1
                elif s>0:
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

        '''
        #print nums
        if len(nums)<3:
            return []
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (-(nums[i]+nums[j]) in nums[j+1:]):
                    temp=[nums[i],nums[j],-(nums[i]+nums[j])]
                    temp.sort()
                    if temp not in result:
                        result.append(temp)
                        print i,nums[i],j,nums[j]
        return result
        '''

        '''
        nums.sort()
        print nums
        for i in nums:
            if i>=0:
                break
        place = nums.index(i)
        i=0;j=0
        for i in nums[place:-1]:
            for j in nums[nums.index(i)+1:]:
                if i==0 and j==0:
                    if nums.count(0) >= 3:
                        if [-(i+j),i,j] not in result:
                            result.append([-(i+j),i,j])
                elif -(i+j) in nums:
                    if [-(i+j),i,j] not in result:
                        result.append([-(i+j),i,j])
                        #print "*",result
        for i in nums[:place-1]:
            for j in nums[nums.index(i)+1:place]:
                if -(i+j) in nums:
                    if [i,j,-(i+j)] not in result:
                        result.append([i,j,-(i+j)])
        #print result
        return result
        '''
if __name__ == '__main__':
    example = Solution()
    nums=[-1,0,1,2,-1,-4]
    #nums=[-1,-2,-3,4,1,3,0,3,-2,1,-2,2,-1,1,-5,4,-3]
    #nums=[1,2,-2,-1]
    print nums
    print example.threeSum(nums)



