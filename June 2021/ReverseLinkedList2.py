'''
Reversing list from left to right
'''

def reverseList(head,left,right):
    dummy = pre =  ListNode(0)
    dummy.next = head

    for _ in range(left-1):
        pre = pre.next
    curr = pre.next

    node = None
    for _ in range(right-left+1):
        new = curr.next
        curr.next = node
        node = curr
        curr = new

    pre.next.next  =curr
    pre.next = node
    return dummy.next
    
    