class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        ints=[0,1,5,10,50,100,500,1000]
        strs=['0','I','V','X','L','C','D','M']
        if len(s)<2:
            return ints[strs.index(s)]
        else:
            count=0
            s=s+'00'
            j=strs.index(s[0])
            jj=strs.index(s[1])
            i=2
        while 1:
            if i>=len(s):
                break
            jjj=strs.index(s[i])
            if j>jj:
                count=count+ints[j]
            elif j<jj:
                count=count-ints[j]
            else:
                if jjj>jj:
                    count=count-ints[j]
                else:
                    count=count+ints[j]
            print count,ints[j],ints[jj],ints[jjj]
            i=i+1
            j=jj
            jj=jjj
        return count
if __name__ == '__main__':
    example = Solution()
    s="DCXXI"
    print example.romanToInt(s)