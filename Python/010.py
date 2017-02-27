class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s)==0 or len(p)==0:
            return False
        ss=pp=0
        flag=0

        while 1:
            print "roll",ss,pp
            if ss==len(s) and pp==len(p):
                break
            elif ss==len(s) and pp < len(p):
                return False
            elif ss<len(s) and pp==len(p):
                return False

            if p[pp]=='.':
                if pp+1==len(p):
                    flag=1
                elif p[pp+1]=='*':
                    flag=3
                    #.*
                else:
                    flag=1
                    #.a
            else:
                #aa+a*
                #a*
                if pp+1==len(p):
                    flag=1
                elif p[pp+1]=='*':
                    flag=2
                else:
                #aa
                    flag=0

            if flag == 0:#a
                if s[ss] != p[pp]:
                    return False
                ss+=1
                pp+=1
                print "flag=%d"%flag
                print '      ',s,ss,len(s)
                print '      ',p,pp,len(p)
            elif flag == 1:#.
                ss+=1
                pp+=1
                print "flag=%d"%flag
                print '      ',s,ss,len(s)
                print '      ',p,pp,len(p)
            elif flag == 2:#a*
                print "flag=%d"%flag
                print '      ',s,ss,len(s)
                print '      ',p,pp,len(p)
                p1=pp
                while pp+3 <len(p):
                    print p,pp,len(p)
                    if p[pp+3] == '*':
                        pp=pp+2
                    else:
                        break
                print "###",p,pp,len(p)
                if pp+2>=len(p):
                    #aa
                    #a*
                    while ss<len(s):
                        if s[ss] != p[pp]:
                            break
                        ss=ss+1
                    if ss+1 == len(s):
                        return True
                    pp=pp+2
                elif pp+2<len(p):#a*b*cc
                    pp=pp+2
                    s1=ss
                    print "&flag=%d"%flag
                    print '      ',s,ss,len(s),s1
                    print '      ',p,pp,len(p),p1
                    if p[p1]==p[pp]:
                        p2=pp
                        while pp+1<len(p):
                            if p[p2]==p[pp+1]:
                                pass
                            else:
                                break
                            pp=pp+1
                        print "&flag=%d"%flag
                        print '      ',s,ss,len(s),s1
                        print '      ',p,pp,len(p),p1
                        if pp+1 == len(p) and p[p2]==p[pp]:
                            #aaaa
                            #a*aa
                            print  "hello",p[p2]
                            while ss<len(s):
                                if s[ss] == p[p2]:
                                    ss=ss+1
                                else:
                                    break
                            print ss,s1,pp,p2
                            if ss==len(s):
                                if ss-s1 < pp-p2+1:
                                    return False
                            pp=pp+1
                            print ss,pp
                            continue
                        elif pp+1 < len(p) and p[pp+1]=='*':
                            #aaaaaaaaaaaaa
                            #aa*aa*a*a*aaa
                            print "ssss",ss,pp,p2
                            p3=0
                            while pp+1<len(p):
                                if p[pp+1] =='*':
                                    p3=p3+1
                                elif p[pp+1] != p[p2]:
                                    break
                                pp=pp+1
                            s1=ss
                            print "ssss",ss,pp,p2,p3
                            while ss<len(s):
                                if s[ss] == p[p2]:
                                    ss=ss+1
                                else:
                                    break
                            print "sss1",ss,pp,p2,p3,s1
                            if ss==len(s):
                                if ss-s1 < pp-p3-p3:
                                    return False
                            print "sss2",ss,pp,p2,p3,s1
                            pp=pp+1
                            continue
                        elif pp+1 < len(p) and p[pp+1]!=p[p2]:
                            #aaaaa
                            #a*aab
                            pp=pp+1
                            s1=ss
                            print "sss2",ss,pp,s1
                            while ss<len(s):
                                if s[ss] == p[p2]:
                                    ss=ss+1
                                elif s[ss] == p[pp]:
                                    if (ss-s1) < (pp-p2):
                                        return False
                                    else:
                                        break
                                else:
                                    return False
                            continue
                        else:
                            print "tttt",ss,pp
                            print "tflag=%d"%flag
                            print '      ',s,ss,len(s),s1
                            print '      ',p,pp,len(p),p1
                            continue


                    while ss+1<len(s):
                        if s[ss] == p[pp]:
                            break
                        ss=ss+1
                    print ">>flag=%d"%flag
                    print '      ',s,ss,len(s),s1
                    print '      ',p,pp,len(p),p1
                    if ss+1 ==len(s) and s[ss]!=p[pp]:#modify
                        #abcd
                        #abcd*p
                        return False
                    else:
                        # ss=ss+1
                        #aabcdefg
                        #aa*b*c*g
                        print ">>>flag=%d"%flag
                        print '      ',s,ss,len(s),s1
                        print '      ',p,pp,len(p),p1
                        while s1<=ss and p1<=pp:
                            print "***flag=%d"%flag
                            print '      ',s,ss,len(s),s1
                            print '      ',p,pp,len(p),p1
                            if s[s1]==p[p1]:
                                s1=s1+1
                                print "ss",s1
                            else:
                                if p[p1] == '.':
                                    break
                                p1=p1+2
                                print "*1flag=%d"%flag
                                print '      ',s,ss,len(s),s1
                                print '      ',p,pp,len(p),p1
                                while p1 < pp:
                                    if p[p1] == p[p1-2]:
                                        p1=p1+2
                                    else:
                                        break

                                print "*2flag=%d"%flag
                                print '      ',s,ss,len(s),s1
                                print '      ',p,pp,len(p),p1
                        # print "flag=%d"%flag
                        # print '      ',s,ss,len(s),s1
                        # print '      ',p,pp,len(p),p1
                        if p1>=len(p):
                            continue
                        if p[p1] == '.':
                            #abcdef
                            #aa*.*f
                            pass
                        elif s1 == ss and p1==pp:
                            #abcdef
                            #aa*b*f
                            return False
                print "flag=%d"%flag
                print '      ',s,ss,len(s)
                print '      ',p,pp,len(p)
                
            else:#.*
                print "flag=%d"%flag
                print '      ',s,ss,len(s)
                print '      ',p,pp,len(p)
                p1=pp
                while pp+3<len(p):
                    if p[pp+3] == '*':
                        pp=pp+2
                    else:
                        break
                if pp+2==len(p):
                    return True
                else:
                    pp=pp+2
                print "flag=%d"%flag
                print '      ',s,ss,len(s)
                print '      ',p,pp,len(p)
                if ss-1<0:
                    ss=0
                else:
                    ss=ss-1
                while ss+1 < len(s):
                    if p[pp]!=s[ss]:
                        ss=ss+1
                    else:
                        break
                print "flag=%d"%flag
                print '      ',s,ss,len(s)
                print '      ',p,pp,len(p)
                if ss+1==len(s) and s[ss]!=p[pp]:
                    #aa
                    #.*b
                    return False
                print "flag=%d"%flag
                print '      ',s,ss,len(s)
                print '      ',p,pp,len(p)
                
        return True



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
    s="aaa"
    p="ab*a*c*a"
    print example.isMatch(s,p)
