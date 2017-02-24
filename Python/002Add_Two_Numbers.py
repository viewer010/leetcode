#coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def add(self,x):
        nexts=self
        while nexts.next:
            nexts=nexts.next
        new = ListNode(x)
        nexts.next=new
    def display(self):
        nexts=self
        i=1
        while nexts:
            print "%d -> %d"%(i,nexts.val)
            nexts=nexts.next
            i+=1

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1 = l1
        ll2 = l2
        lresult = None
        r = (ll1.val+ll2.val) % 10
        d = (ll1.val+ll2.val) / 10
        lresult =  ListNode(r)
        nexts = lresult
        ll1 = ll1.next
        ll2 = ll2.next
        temp = ListNode(0)
        while ll1 or ll2 or d:
            if not ll1:
                ll1=temp
            if not ll2:
                ll2=temp
            r = (ll1.val+ll2.val+d)%10
            new = ListNode(r)
            nexts.next=new
            nexts = nexts.next
            d =(ll1.val+ll2.val+d)/ 10
            ll1 = ll1.next
            ll2 = ll2.next
        return lresult
            


if __name__ == '__main__':
    new = ListNode(1)
    print "new"
    new.display()
    
    new1 = ListNode(9)
    new1.add(9)
    print "new1"
    new1.display()

    ss= Solution()
    result = ss.addTwoNumbers(new,new1)
    print "result"
    result.display()
        