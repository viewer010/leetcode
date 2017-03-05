# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count=0
        i=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        temp=head
        if n==count:
            temp=head
            head=head.next
            temp.next=None
            del temp
            return head
        while temp:
            if i+1==count-n:
                temps=temp.next
                temp.next=temp.next.next
                del temps
                break
            i=i+1
            temp=temp.next
        return head


    '''
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        heads=self.reverse(head)
        if n==1:
            heads=heads.next
        else:
            i=1
            temp = heads
            while heads:
                if i+1 == n:
                    if heads.next:
                        heads.next=heads.next.next
                        break
                    else:
                        pass
                heads=heads.next
                i=i+1
            heads=temp
        return self.reverse(heads)

    def reverse(self,head):
        
        if head:
            heads=ListNode(head.val)
            head=head.next
        else:
            return None
        while(head):
            temp=ListNode(head.val)
            temp.next=heads
            heads=temp
            head=head.next
        return heads
    '''
    def add(self,head,value):
        while head.next:
            head=head.next
        temp=ListNode(value)
        head.next=temp
        return head
    def display(self,head):
        while head:
            print head.val,
            head=head.next
        print 

if __name__ == '__main__':
    example = Solution()
    head = ListNode(1)
    # example.add(head,2)
    # example.add(head,3)
    # example.add(head,4)
    # example.add(head,5)
    example.display(head)
    # heads=example.reverse(head)
    # example.display(heads)
    heads=example.removeNthFromEnd(head,1)
    example.display(heads)
