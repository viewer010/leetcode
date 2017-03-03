class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i=0
        flag=0
        while 1:
            if i == len(str):
                break
            if str[i]==' ':
                if flag==0:
                    i=i+1
                    continue
            if str[i]=='+' or str[i]=='-':
                if flag ==0:
                    flag=1
                    i=i+1
                    continue
                elif flag==1:
                    break
            if str[i]<='9' and str[i]>='0':
                flag=2
            if str[i]>'9' or str[i]<'0':
                break
            i=i+1
        print "flag=",flag
        if flag <2:
            return 0
        if i==0:
            return 0
        print "*",i
        result = int(str[:i])
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return result

if __name__ == '__main__':
    example=Solution()
    strs="-abc"
    #strs="+1"
    #strs="+-2"
    #strs="123  456"
    #strs='  -0012a42'
    #strs='123a'
    #print "strs="
    print example.myAtoi(strs)