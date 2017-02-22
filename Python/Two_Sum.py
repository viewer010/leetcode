'''
1.if temp1 in nums:  x
2.if temp1 in nums and nums.index(temp)!=nums.index(temp1): x
3.nums[num]=-temp  0,2,3,0 0
4.nums[num]='a'   Time Limit Exceeded

'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        rlist=[]
        for temp in nums:
            temp1=target - temp
            print("temp=%d temp1=%d"%(temp,temp1))
            num=nums.index(temp)
            nums[num]='a'
            if temp1 in nums:
                rlist.append(num)
                rlist.append(nums.index(temp1))
                return rlist
            nums[num]=temp
        '''
        rlist=[]
        for i in range(len(nums)):
            temp1=target - nums[i]
            print("temp=%d temp1=%d"%(temp,temp1))
            nums[i]='a'
            if temp1 in nums:
                rlist.append(i)
                rlist.append(nums.index(temp1))
                return rlist
            nums[i]=temp

if __name__ == '__main__':
    nums = [3,2,3]
    target = 5
    Solution = Solution()
    glist=Solution.twoSum(nums,target)
    print "hello"
    print glist
    