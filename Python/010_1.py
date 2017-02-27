#coding=utf8
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        pattern = re.compile(p)
        match = pattern.match(s)
        if match:
            # 使用Match获得分组信息
            #print match.group()
            return match.group(0)==s
        else:
            return False



if __name__ == '__main__':
    example = Solution()
    #s="abcd"
    #p="abcd*"
    #s="aaab"
    #p=".*ab"
    #s="bbbba"
    #p=".*a*a"
    #s="aaa"
    #p="ab*ac*a"
    #s="aab"
    #p="c*a*b"
    #s="aab"
    #p="a*a*a*d*b"
    #s="aaaaab"
    #p="a*aab"
    #s="aab"
    #p="a.*b"
    #s="aabcaabaccbcaaaacbc"
    #p="ac*a*b*a*c*c*a*ac*c"
    #s="aaa"
    #p="a*a"
    #s="abcaabccccacbbcba"
    #p="a*.*ac*bb*.*b*aa*c"
    s=""
    p="ab*a*c*a"
    print example.isMatch(s,p)
