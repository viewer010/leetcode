class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1=[]
        list2=[]
        i=0
        count=0
        if not len(s):
            return 0
        while 1:
            if i >= len(s):
                break
            list2.append(count)
            for ii in s[i:]:
                i=i+1
                print list2,"|",list1,count
                if ii not in list1:
                    list1.append(ii)
                    list2[len(list2)-1]+=1
                    #print list2,"|",list1
                else:
                    count = len(list1)-list1.index(ii)
                    temp = ii
                    list1=list(s[i-count:i])
                    #print "after",list1
                    break
        #print list1
        return max(list2)


if __name__ == '__main__':
    s=Solution()
    strs="pwwkew"
    print s.lengthOfLongestSubstring(strs)