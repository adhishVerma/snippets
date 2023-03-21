class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = None 
    self.size = 0



  def prepend(self,data) -> None:
    """
    adds to the front of the linked list
    """
    newHead =  Node(data)
    newHead.next = self.head
    self.head = newHead
    self.size += 1


  def append(self, data) -> None:
    """
    adds to the end of linked list
    """
    if(self.head == None):
      head =  Node(data)
      self.head = head
      self.size += 1
      return

    current  = self.head
    while  (current.next != None):
      current = current.next
    current.next = Node(data)
    self.size += 1


  def delete(self,data):
    """
    deletes the value inside linked list 
    """
    if(self.head == None): return

    if(self.head.data == data):
      self.head = self.head.next
      self.size -= 1
      return

    current = self.head
    while (current.next != None):
      if(current.next.data == data):
        current.next = current.next.next
        self.size -= 1
        return
      current = current.next


  def clear(self):
    """
    clears the LL and makes it empty
    """
    temp = self.head
    self.head = None
    while (temp != None):
      temp2 = temp
      temp = temp.next
      del temp2
      self.size -= 1
  
  

  def search(self, value):
    """
    searches for a value in LL and returns the pointer to the node that contains the value if such node exists
    """
    temp = self.head
    while (temp != None):
      if (temp.data == value):
        return temp
      temp  = temp.next
    return None
  

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
    temp.next = newNode
    self.size += 1
      
# returns the size of linked list
  def __len__(self):
    return self.size

# repr
  def __repr__(self) -> str:

    if self.head == None:
      return "<empty>"

    res = "<"
    current = self.head
    while current.next != None:
      res += str(current.data)+","
      current = current.next
    res += str(current.data) +">"
    return res
    

    

ll = LinkedList()
ll.append(3)
ll.append(4)
ll.append(5)
print(ll)
ll.append(6)
ll.prepend(2)
ll.prepend(1)
print(ll)
print(len(ll))
ll.delete(2)
print(ll)
print(len(ll))
ll.delete(1)
print(ll)
print(len(ll))
ll.append(7)
print(ll)
ll.insert(4,8)
print(ll)
print(ll.search(8))
ll.insert(0,1)
ll.insert(1,2)
print(ll)
