#coding=utf8
'''
该问题解的个数就是卡特兰数，但是现在不是求个数，而是要将所有合法的括号排列打印出来。
       该问题和《编程之美》的买票找零问题一样，通过买票找零问题我们可以知道，针对一个长度为2n的合法排列，第1到2n个位置都满足如下规则：左括号的个数大于等于右括号的个数。所以，我们就可以按照这个规则去打印括号：假设在位置k我们还剩余left个左括号和right个右括号，如果left>0，则我们可以直接打印左括号，而不违背规则。能否打印右括号，我们还必须验证left和right的值是否满足规则，如果left>=right，则我们不能打印右括号，因为打印会违背合法排列的规则，否则可以打印右括号。如果left和right均为零，则说明我们已经完成一个合法排列，可以将其打印出来。通过深搜，我们可以很快地解决问题，
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results=[]
        left,right=n,n
        result=''
        def getParenthesis(left, right,results,result):
            if left==0 and right==0:
                #print 1,results,result
                results.append(result)
            if left>0:
                #print 2,results,result
                getParenthesis(left-1,right,results,result+'(')
            if right>0 and left<right :
                #print 3,results,result
                getParenthesis(left,right-1,results,result+')')
        getParenthesis(left,right,results,result)
        return results

if __name__ == '__main__':
    example = Solution()
    n=0
    #example.generateParenthesis(n)
    print len(example.generateParenthesis(n)),example.generateParenthesis(n)
        