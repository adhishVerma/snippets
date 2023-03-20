class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None
    self.prev = None

class DoubleLL:
  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.size = 0
  
# returns length of the linked list 
  def __len__(self):
    return self.size

# adds to the end of a doubly linked list
  def append(self,data):
    if self.head == None:
      temp = Node(data)
      self.head = temp
      self.tail = temp
    else:
      current = self.tail
      temp = Node(data)
      current.next = temp
      temp.prev = current
      self.tail = temp
    self.size += 1
    return

# adds an element to the start of a linked list
  def prepend(self,data):
    if self.head == None:
      self.append(data)
    else:
      temp = Node(data)
      current = self.head
      current.prev = temp
      temp.next = current
      self.head = temp
    self.size += 1
    return

