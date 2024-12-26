"""
Coding Exercise: Design a Singly Linked List
Question :

Construct Singly Linked List - Design a Singly linked list class that has a head and tail. Every node is to have two attributes: value:  the value of the current node, and next: a pointer to the next node. The linked list is to be 0-indexed. The class should support the following:

SinglyLinkedList() Initializes the SinglyLinkedList object.

get(index) Get the node at the index passed. If the index is invalid, return -1.

addAtHead(value)- Add a node of given value before the first element of the linked list. Return the SLL

addAtTail(value) -  Add a node of given value at the last element of the linked list. Return the SLL

addAtIndex(index, value) Add a node of given value before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, don’t insert the node(return a message 'invalid index' ). Return SLL once done.

deleteAtIndex(index) Delete the indexth node in the linked list, if the index is valid, else nothing happens.Return deleted node
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    #TC=O(n) SC=O(1)
    def get(self, index):

        if index<0 or index>=self.size:
            return -1
        
        current=self.head
        counter=0
        while counter != index:
            current = current.next
            counter+=1
        return current

# addAtHead(value)- Add a node of given value before the first element of the linked list. Return the SLL
    #TC=O(1) SC=O(1)
    def addAtHead(self, value):
        
        node = Node(value)
        # if self.head==None:
        if not self.head:
            self.head=node
            self.tail=node
        else:
            node.next = self.head
            self.head=node
        self.size+=1

    #TC=O(1) SC=O(1)
    def addAtTail(self, value):

        node = Node(value)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        self.size+=1

    #TC=O(n) SC=O(1)
    def addAtIndex(self, index, value):
        if index < 0 or index > self.size:
            return "invalid index"
        
        if index==0:
            return self.addAtHead(value)
        if index==self.size:
            return self.addAtTail(value)

        node=Node(value)        
        prev=self.get(index-1)
        temp=prev.next
        prev.next=node
        node.next=temp

        self.size+=1

    #TC=O(n) SC=O(1)
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return "invaild index"
        if index==0:
            temp=self.head
            self.head=temp.next
            self.size-=1
            if self.size==0:
                self.tail=None
            return temp.value
        
        if index==self.size-1:
            prev=self.get(index-1)
            new=self.tail
            prev.next=None
            self.tail=prev
            self.size-=1
            return new.value
        
        prev=self.get(index-1)
        new=prev.next
        prev.next=new.next
        self.size-=1
        return new.value

#7,6,8,12,90

llist=SingleLinkedList()
# print(llist.get(0))
print(llist.addAtHead(7))
print(llist.addAtTail(8))
print(llist.addAtTail(90))
print(llist.addAtIndex(2,12))
# print(llist.get(0))
# print(llist.get(1))
# print(llist.get(2))
print(llist.addAtIndex(1,6))
print(llist.get(0).value)
print(llist.get(1).value)
print(llist.get(2).value)
print(llist.get(3).value)
print(llist.get(4).value)
print(llist.get(5))
#7,6,8,12,90
print(llist.deleteAtIndex(1))
print(llist.deleteAtIndex(3))
print(llist.deleteAtIndex(5))

