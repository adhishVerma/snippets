class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.left  = None
    self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# def depthFirstValues(root):

#   if(root == None):
#     return []

#   result = []
#   stack = [root]
#   while(stack):
#     current = stack.pop()
#     result.append(current)
#     if(current.right):
#       stack.append(current.right)
#     if(current.left):
#       stack.append(current.left)
#   return result


# def depthFirstValues(root):
#   if(root == None):
#     return []
#   left = depthFirstValues(root.left)
#   right = depthFirstValues(root.right)
#   return [root.data] + left + right



# def breadthFirstValues(root):
#   if  root == None: return  []
#   result = []
#   queue = [root]
#   while(queue):
#     current = queue.pop(0)
#     result.append(current.data)
#     if current.left:
#       queue.append(current.left)
#     if current.right:
#       queue.append(current.right)
#   return result

# using BFS
# def includes(root,data):
#   if root == None : return False
#   queue = [root]
#   while (queue):
#     current = queue.pop(0)
#     if data == current.data:
#       return True
#     if current.left:
#       queue.append(current.left)
#     if current.right:
#       queue.append(current.right)
#   return False


# using DFS recursion
# def includes(root,data):
#   if root == None: return False
#   if root.data == data: return True
#   left = includes(root.left,data)
#   right = includes(root.right,data)
#   return left or right




"""
        a
       / \
      b   c
     / \   \
    d   e   f 
"""
