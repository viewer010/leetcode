class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        ret=False
        sleft=['(','{','[']
        sright=[')','}',']']
        i=0
        while i!=len(s):
            print "i=",i,
            if s[i] in sleft:
                stack.append(s[i])
            else:
                if not len(stack):
                    ret=False
                    print "here1"
                    break
                temp=stack.pop()
                if temp!=sleft[sright.index(s[i])]:
                    print "here2",temp,sleft[sright.index(s[i])],s[i]
                    ret=False
                    break
            i+=1
            print '*',stack,ret,i
        print 
        print "**",stack,ret,i,len(s)
        if len(stack)==0 and i==len(s):
            ret=True
        else:
            ret=False
        return ret
if __name__ == '__main__':
    example = Solution()
    s="([])"
    print example.isValid(s)


