class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1:
            return s
        lists=[]
        for i in range(numRows):
            list1=[]
            lists.append(list1)
        temp = 0
        flag = 1
        for i in range(0,len(s)):
            lists[temp].append(s[i])
            if temp == len(lists)-1:
                flag=-1
            if temp == 0:
                flag=1
            temp += flag
        rlist=[]
        for i in lists:
            rlist+=i
        return "".join(rlist)

if __name__ == '__main__':
    example = Solution()
    s="AB"
    num=1
    print example.convert(s,num)

