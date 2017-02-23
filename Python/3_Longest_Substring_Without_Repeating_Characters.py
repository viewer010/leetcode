class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1=[]
        list2=[]
        for i in range(len(s)):
            list2.append(0)
            list1=[]
            for ii in s[i:]:
                if ii not in list1:
                    list1.append(ii)
                    list2[i]+=1
                else:
                    break
        print list2
        return max(list2)


if __name__ == '__main__':
    s=Solution()
    strs="pwwkew"
    print s.lengthOfLongestSubstring(strs)