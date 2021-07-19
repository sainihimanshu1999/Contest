'''this is similary to reversing the linked list but quite complicated indeed'''


def reverseKgroups(head,k):
    dummy = ListNode(0)
    curr,prev,nxt = dummy,dummy,dummy
    dummy.next = head

    count = 0

    while curr.next:
        count+=1
        curr = curr.next

    while count>=k:
        curr=new=prev.next
        nxt = curr.next

        for _ in range(k-1):
            temp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt= temp

        prev.next = curr
        new.next = nxt
        prev = new
        count -=k
    
    return dummy.next
    
