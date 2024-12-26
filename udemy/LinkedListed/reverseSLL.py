"""
Coding Exercise: Reverse SLL
Question :

Reverse SLL- You are given the head of a Singly Linked list. 
Write a function that will take the given head as input, reverse the Linked List 
and return the new head of the reversed Linked List.
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseSLL(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def printLL(head):
    current = head
    listed = []
    while current is not None:
        listed.append(current.val)
        current = current.next
    return listed

# Creating the linked list
head = Node(1)
head.next = Node(1)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(3)

# Printing the original linked list
print(printLL(head))

# Reversing the linked list
reversed_head = reverseSLL(head)

# Printing the reversed linked list
print(printLL(reversed_head))