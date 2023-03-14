class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = None 

  def prepend(self,data) -> None:
    newHead =  Node(data)
    newHead.next = self.head
    self.head = newHead


  def append(self, data) -> None:
    if(self.head == None):
      head =  Node(data)
      self.head = head
      return

    current  = self.head
    while  (current.next != None):
      current = current.next
    current.next = Node(data)

  def deleteValue(self,data):
    if(self.head == None): return
    if(self.head.data == data):
      self.head == self.head.next
      return

    current = self.head
    while (current.next != None):
      if(current.next.data == data):
        current.next = current.next.next
        return
      current = current.next