# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        index=head
        l11,l22=l1,l2
        while True:
            if l11 and l22:
                print l11.val,l22.val
                if l11.val<l22.val:
                    temp=ListNode(l11.val)
                    l11=l11.next
                else:
                    temp=ListNode(l22.val)
                    l22=l22.next
                index.next=temp
                index=temp
            else:
                break
        while l11:
            temp=ListNode(l11.val)
            index.next=temp
            index=temp
            l11=l11.next
        while l22:
            temp=ListNode(l22.val)
            index.next=temp
            index=temp
            l22=l22.next
        return head.next
        
    def display(self,head):
        index=head
        lists=[]
        while index:
            lists.append(index.val)
            index=index.next
        return lists
    def add(self,head,value):
        while head.next:
            head=head.next
        temp=ListNode(value)
        head.next=temp
        return head
if __name__ == '__main__':
    example=Solution()
    example = Solution()
    head = ListNode(5)
    example.add(head,3)
    example.add(head,1)
    print example.display(head)

    head1 = ListNode(6)
    example.add(head1,4)
    example.add(head1,2)
    print example.display(head1)

    head3 = example.mergeTwoLists(head,head1)
    print example.display(head3)
    # heads=example.reverse(head)
    # example.display(heads)



