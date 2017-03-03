class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''
        #first
        if x<0:
            return False
        xx=int(str(x)[::-1])
        return xx == x
        '''
        s=str(x)
        start=0
        end=len(s)-1
        while end>=start:
            if s[start] != s[end]:
                return False
            end -= 1
            start += 1
        return True
if __name__ == '__main__':
    example = Solution()
    x="-1"
    print example.isPalindrome(x)