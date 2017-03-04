class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        maps=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        ret=[]
        temp=''
        if not len(digits):
            return ret
        for temp in digits:
            print temp
            if temp !=1:
                ret=list(maps[int(temp)])
                break
        temp=digits.index(temp)+1
        for i in digits[temp:]:
            ret=[ x+y for x in ret for y in maps[int(i)]]
        return ret
if __name__ == '__main__':
    example=Solution()
    nums='2'
    print example.letterCombinations(nums)