class Node:
    def __init__(self, value):
        self.val=value
        self.next=None

def removeDuplicates(head):
    current = head

    while current!=None:
        temp=current
        if temp.next is not None and temp.val==temp.next.val:
            temp.next=temp.next.next
            current = temp
        else:
            current = current.next

    return head

def printLL(head):
    current=head
    listed=[]
    while current!=None:
        listed.append(current.val)
        current=current.next
    return listed

head=Node(1)
head.next=Node(1)
head.next.next=Node(1)
head.next.next.next=Node(2)
head.next.next.next.next=Node(2)
head.next.next.next.next.next=Node(3)
print(printLL(head))

llist = removeDuplicates(head)
print(printLL(llist))
# print(llist.val)
# print(llist.next.val)
# print(llist.val)
# print(llist.val)