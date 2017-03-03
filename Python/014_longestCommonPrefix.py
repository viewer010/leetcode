class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs):
            return ""
        lens = len(strs)
        count=0
        temp=''
        while 1:
            if len(strs[0])>count:
                temp=strs[0][count]
            else:
                return strs[0][:count]
            for i in range(1,lens):
                if len(strs[i])<=count:
                    return strs[i][:count]
                if strs[i][count] == temp:
                    continue
                else:
                    return strs[i][:count]
            count+=1
            #print "count=",count
        return strs[0]
if __name__ == '__main__':
    example = Solution()
    strs=["11","1",""]
    print "restult=",example.longestCommonPrefix(strs)



