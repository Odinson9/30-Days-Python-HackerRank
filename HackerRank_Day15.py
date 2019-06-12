class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
        if head == None: # if empty link
            self.head = Node(data)  # head becomes Node trying to be inserted     
        else: # if link has length of at least 1
            current = self.head # pointer starts at head
            while current.next: # infinite loop until false
                current = current.next # pointer iterates through each node
            current.next = Node(data) # assign null node to Node(data) trying to be inserted
        return self.head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  