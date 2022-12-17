from collections import deque
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
Q = deque()
def insertValue(data, root):
    newnode = Node(data)
    if Q:
        temp = Q[0]
    if root == None:
        root = newnode
    elif temp.left == None:
        temp.left = newnode
    elif temp.right == None:
        temp.right = newnode
        Q.popleft()
    Q.append(newnode)
    return root
def createTree(a, root):
    for i in range(len(a)):
        root = insertValue(a[i], root)
    return root
def height(node):
	if node is None:
		return 0
	else:
		leftHeight = height(node.left)
		rightHeight = height(node.right)
		if leftHeight > rightHeight:
			return leftHeight+1
		else:
			return rightHeight+1
a = [int(x) for x in input().split()]
root = createTree(a, None) 
print(height(root))