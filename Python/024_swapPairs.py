# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        heads=head
        next2=heads
        while True:
            if head and head.next:
                head.val,head.next.val=head.next.val,head.val
            else:
                break
            head=head.next.next
        return heads

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
    head1=tolist([1,2,3,4])
    display(head1)
    example=Solution()
    head=example.swapPairs(head1)
    display(head)