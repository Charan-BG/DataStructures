"""
Coding Exercise: Cycle Detection
Question:

Cycle Detection - You are given the head of a linked list. 
Check if there is a cycle and if yes,  return the node where the cycle begins. 
If there is no cycle, return null. There is a cycle in a linked list if there is some node 
in the list that can be reached again by continuously following the next pointer. 
Do not modify the linked list.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def cycleDetection(head):

    if not head or not head.next:
        return None
    
    hare=head
    tortoise=head
    while hare and hare.next:
        hare = hare.next.next
        tortoise=tortoise.next
        if tortoise==hare:
            break

    if hare != tortoise:
        return None
    
    pointer=head
    while pointer!=tortoise:
        pointer=pointer.next
        tortoise=tortoise.next

    return tortoise

one=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)

one.next=two
two.next=three
three.next=four
four.next=five
five.next=four

head=one
print(cycleDetection(head).val)

