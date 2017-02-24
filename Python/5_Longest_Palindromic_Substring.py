#coding=utf8
class Solution(object):
    def longestPalindrome(self,s):
        dicts=[]
        dicta=[]
        maxs=''
        for i in range(len(s)):
            if s[i] not in dicta:
                dicta.append(s[i])
                dict1=[]
                dict1.append(i)
                dicts.append(dict1)
            else:
                dicts[dicta.index(s[i])].append(i)
        print dicts
        print dicta
        for i in range(len(dicta)):
            dict_t=dicts[i]
            print dict_t
            if len(dict_t)>1:
                for j in range(len(dict_t)):
                    for jj in dict_t[j+1:]:
                        print dict_t,j,jj,dict_t[j+1:],jj-dict_t[j]+1,s[dict_t[j]:jj+1],s[dict_t[j]:jj+1][::-1]
                        if jj-dict_t[j]+1 > len(maxs):
                            if s[dict_t[j]:jj+1] == s[dict_t[j]:jj+1][::-1]:
                                if len(s[dict_t[j]:jj+1])>len(maxs):
                                    maxs=s[dict_t[j]:jj+1]
            elif len(maxs)<=1:
                maxs=dicta[i]
        print maxs
        return maxs
                
if __name__ == '__main__':
    a=Solution()
    s="babad"
    a.longestPalindrome(s)
                
