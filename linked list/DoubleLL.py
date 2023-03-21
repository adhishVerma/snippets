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
  
  def append(self,data):
    """
    adds to the end of a doubly linked list
    """
    if self.head == None:
      temp = Node(data)
      self.head = temp
      self.tail = temp
    else:
      temp = Node(data)
      self.tail.next = temp
      temp.prev = self.tail
      self.tail = self.tail.next
    self.size += 1
    return


  def prepend(self,data):
    """
    adds an element to the start of a doubly  linked list
    """
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


  def peekFirst(self):
    """
    returns the value of first node
    """
    if self.size == 0 : raise Exception("List is empty")
    return self.head.data


  def peekLast(self):
    """
    return the value of the last node
    """
    if self.size == 0 : raise Exception("List is empty")
    return self.tail.data
  

  def clear(self):
    """
   clear the list
    """
    temp = self.head
    self.head = None
    self.tail = None
    while (temp != None):
      temp2 = temp
      temp = temp.next
      del temp2
      self.size -= 1


  def pop(self):
    """
    pops the last element of the list and returns its value
    """
    if self.size == 0: raise Exception("List is empty")

    temp = self.tail
    self.tail = temp.prev
    temp.prev = None
    self.tail.next = None
    self.size -= 1
    return temp.data


  def shift(self):
    """
    removes the first element and returns its value
    """
    if self.size == 0: raise Exception("List is empty")

    temp = self.head
    self.head = temp.next
    temp.next = None
    self.head.prev = None
    self.size -= 1
    return temp.data
  
  def insert(self,pos,data):
    """
   inserts a node at the specified index
    """
    if self.head == None:
      raise Exception('Linked list is empty')
    
    if pos < 0:
      raise Exception('Index pos can\'t be negative')

    if pos == 0:
      self.prepend(data)
      return

    if pos == self.size - 1:
      self.append(data)
      return

    temp = self.head
    for i in range(pos-1):
      temp = temp.next
    newNode = Node(data)
    newNode.next = temp.next
    newNode.prev = temp
    temp.next = newNode
    self.size += 1
    


  def __len__(self):
    """
    returns length of the linked list 
    """
    return self.size


  def __repr__(self) -> str:

    if self.head == None:
      return "<empty>"

    res = "<"
    current = self.head
    while current.next != None:
      res += str(current.data)+","
      current = current.next
    res += str(current.data) + ">"
    return res



dll = DoubleLL()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
print(dll.peekFirst())
print(dll.peekLast())
print(dll.shift())
print(dll.pop())
print(dll.insert(1,3))

print(dll)

