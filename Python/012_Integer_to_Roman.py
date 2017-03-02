class Solution(object):

    def intToRoman(self,num):
        """
        :type num: int
        :rtype: str
        """
        ints=[1,   5, 10, 50, 100,500,1000]
        strs=['I','V','X','L','C','D','M']
        rets=''
        i=6
        count=0
        while num>count:
            if num-count>=ints[i]:
                if not rets:
                    rets=rets+strs[i]
                    flag=1
                elif  flag<=3:
                    if rets[-1]==strs[i]:
                        flag+=1
                    else:
                        flag=1
                    rets=rets+strs[i]
                if flag==4:
                    if len(rets)>4 and ints[strs.index(rets[-5])] == ints[strs.index(rets[-1])+1]:
                        rets=rets[:-5]+rets[-1]+strs[strs.index(rets[-5])+1]
                    else:
                        rets=rets[:-3]
                        rets=rets+strs[i+1]
                    flag=1
                    #if rets[-1]==rets[-3]:
                #print flag,rets[-1]
                count=count+ints[i]

            else:
                i=i-1

        return rets
if __name__ == '__main__':
    example = Solution()
    i=81
    for i in range(1,100):
        print i,example.intToRoman(i)
    print i,example.intToRoman(i)



