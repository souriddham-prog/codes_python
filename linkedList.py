class Node:
    def __init__(self,data):
        self.data=data #value
        self.next=None #next node ref
class LinkedList:
    def __init__(self):
        self.head=None #blank header
    def append(self,data):
        print(f"Append {data} to the list")
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def traverse(self):
        print(f"current state of the list")
        current=self.head
        elements=[]
        while current:
            elements.append(current.data)
            current =current.next
        print(elements)

    def countNodes(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count
    
    def replace(self,data,newdata):
        print(f"replace {data} with {newdata}")
        if not data:
            print("improper")
            return
        
        
        current =self.head
        b=False
        while current:
            if current.data==data:
                current.data=newdata 
                b=True
            current=current.next
        if not b:
            print(f"{data} is absent in the list")
        
    def deleteEnd(self):
        print("delete last node")
        current=self.head
        while current.next.next:
            current=current.next
        print(f"Last element {current.next.data}")
        current.next=None

    def delete_nthNode(self,n):
        print(f"delete node at position {n}")
        if n>self.countNodes():
            print("invalid")

        if n==1:
            print(f"Deleted node value= {self.head.data}")
            self.head=self.next

        current =self.head
        count=1
        while current:
            count+=1
            if count==n:
                break
            current=current.next
        print(f"deleted node value: {current.next.data}")
        current.next=current.next.next

       


mylist=LinkedList()
mylist.append(10)
mylist.append(2)
mylist.append(20)
mylist.append(209)
mylist.traverse()
mylist.deleteEnd()
mylist.traverse()
mylist.replace(10,30)
mylist.traverse()
mylist.replace(15,16)
mylist.append(23)
mylist.traverse()
mylist.replace(2,80)
mylist.traverse()
mylist.replace(23,4)
mylist.traverse()
mylist.delete_nthNode(3)
mylist.traverse()