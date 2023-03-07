class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = None 
    self.tail = None

  def insertHead(self,node:Node) -> None:
    node.next = self.head #pointing the new head to current head
    self.head = node #setting the list head as the  new  node

  def insertTail(self,node:Node) -> None:
    self.tail = node #A single node will point towards None



# creating a LL and printing it
llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third


# we use dummy variable to traverse through list
dummy = llist.head
while(dummy):
  print(dummy.data,end=" ")
  dummy = dummy.next

llist.insertHead(Node(12))

print("\n after inserting head")

dummy = llist.head
while(dummy):
  print(dummy.data,end=" ")
  dummy = dummy.next

