class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
        
        
class cll:
    def _init_(self):
        self.head=None
        self.tail=None
        
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,'-->',end=' ')
            print(temp.next.data)
                
                         
                
    def beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
        
    
    def end(self,data):
        new_node=Node(data)
        if self.tail is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.tail.next=self.head
                
                

    def del_beginning(self):
        if self.head is None:
            print("circular list is not present")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.tail.next=self.head



obj=cll()
node_1= Node("sai")
node_2= Node("poorna")
node_3= Node("chander")
node_4= Node("kumar")
node_5= Node("ravi")
                


node_1.next=node_2
node_2.next=node_3
node_3.next=node_4
node_4.next=node_5
node_5.next=node_1



obj.head=node_1
obj.tail=node_1


obj.head=node_1
obj.head.next=node_2
#obj.tail=node_2
#obj.tail.next=cl.head


obj.beginning(30)
obj.display()