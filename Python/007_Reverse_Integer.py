#coding=utf8
'''
32位计算机字长,用于表示整数,共有2的32平方个.
所以,无符号整数的范围是0~2^32或0~4294967296
带符号整数,因为需要1位来表示+-,所以范围为
-2^31~2^31,或-2147483648~2147483648
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            result=int((str(-x)[::-1]))
            if result > 2147483647:
                return 0
            else:
                return -result
        else:
            result=int(str(x)[::-1])
            if result > 2147483647:
                return 0
            else:
                return result
        
if __name__ == '__main__':
    example = Solution()
    a=0
    print example.reverse(a)