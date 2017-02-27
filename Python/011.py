class Solution(object):
    def maxArea(self, hight):
        """
        :type hights: List[int]
        :rtype: int
        """
        hights=[]
        for i in range(1, len(hight)):
            if hight[i] > hight[i-1]:
                hights.append(hight[i - 1])
            else:
                hights.append(hight[i])

        hmin=min(hights)
        hmax=max(hights)
        maxs= len(hights) * hmin
        for i in range(hmin+1,hmax+1):
            wight=0
            flag=1
            for temp in hights:
                if temp>=i:
                    print "hi",
                    if flag == 0:
                        wight=wight+1
                    else:
                        flag=0
                        wight=1
                    print wight
                else:
                    area=wight*i
                    print area,wight,i
                    if area > maxs:
                        maxs=area
                    flag=1
            area = wight * i
            print area, wight, i
            if area > maxs:
                maxs = area
        return maxs

if __name__ == '__main__':
    example=Solution()
    height=[1,2,3,4]
    print example.maxArea(height)