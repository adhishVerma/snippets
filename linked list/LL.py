class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = None 
    self.size = 0

# returns the size of linked list
  def __len__(self):
    return self.size

# repr
  def __repr__(self) -> str:

    if self.head == None:
      return "<empty>"

    res = ""
    current = self.head
    while current.next != None:
      res += str(current.data)+","
      current = current.next
    res += str(current.data)
    return res
    

# adds to the front of the linked list
  def prepend(self,data) -> None:
    newHead =  Node(data)
    newHead.next = self.head
    self.head = newHead
    self.size += 1

# adds to the end of linked list
  def append(self, data) -> None:
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

# deletes the value inside linked list 
  def delete(self,data):
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

# clears the LL and makes it empty
  def clear(self):
    temp = self.head
    self.head = None
    while (temp != None):
      temp2 = temp
      temp = temp.next
      del temp2
      self.size -= 1
    return
  
  
# searches for a value in LL and returns the pointer to the node that contains the value if such node exists
  def search(self, value):
    temp = self.head
    while (temp != None):
      if (temp.data == value):
        return temp
      temp  = temp.next
    return None
  
# inserts a node after the target value
  def insert(self,pos,value):
    if self.head == None:
      raise Exception('Linked list is empty')
    
    current = self.head
    while current != None:
      if (current.data == pos):
        temp = Node(value)
        temp.next = current.next
        current.next = temp
        return
      current = current.next
  
    

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
