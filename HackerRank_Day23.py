class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self, root):
        queue = [] # empty queue FIFO
        temp_node = root # assigns a temp value to the root node
        queue.append(temp_node) # adds root to queue
        while len(queue) > 0:
            print(queue[0].data, end=" ") # takes first value in queue and prints its data
            temp_node = queue.pop(0) # removes first value and assigns it to temp_node
            if temp_node.left: # if left child exists
                queue.append(temp_node.left)
            if temp_node.right: # if right child exists
                queue.append(temp_node.right)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)