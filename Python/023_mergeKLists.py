#coding=utf8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ret=[]
        for i in lists:
            while i:
                ret.append(i.val)
                i=i.next
        ret.sort()
        head=ListNode(0)
        next=head
        for i in ret:
            temp=ListNode(i)
            next.next=temp
            next=temp
        return head.next
def tolist(lists):
    head=ListNode(0)
    next=head
    for i in lists:
        temp=ListNode(i)
        next.next=temp
        next=temp
    return head.next
def display(head):
    while head:
        print head.val,
        head=head.next
    print 

if __name__ == '__main__':
    head1=tolist([1,2,3])
    head2=tolist([2,4,6])
    display(head1)
    display(head2)
    example=Solution()
    head3=example.mergeKLists([head1,head2])
    display(head3)
    