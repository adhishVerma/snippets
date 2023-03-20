class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.left  = None
    self.right = None


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

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

# def sumOfTree(root):
#   if root == None: return 0
#   left = sumOfTree(root.left)
#   right = sumOfTree(root.right)
#   return root.data + left + right


# print(sumOfTree(a))

# DFS
# def minValue(root):
#   if root == None: return None
#   smallest = float('inf')
#   stack  = [root]
#   while stack:
#     current = stack.pop()
#     if current.data < smallest: smallest = current.data
#     if current.left: stack.append(current.left)
#     if current.right: stack.append(current.right)

#   return smallest

# recursive DFS
# def minValue(root):
#   if root == None: return float('inf')
#   left = minValue(root.left)
#   right = minValue(root.right)

#   return min(root.data, left, right)


# print(minValue(a)) 


def maxPathSum(root):
  # root to leaf
  if root == None: 
    return float("-inf")
  
  if not root.left and not root.right: return root.data

  left = maxPathSum(root.left)
  right = maxPathSum(root.right)

  return root.data + max(left,right)
  

print(maxPathSum(a))


# print(maxPathSum(a.left) + maxPathSum(a.right) + a.data) ##diameter
"""
        a
       / \
      b   c
     / \   \
    d   e   f 
"""
