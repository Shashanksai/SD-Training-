class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_head(self):
        if self.head is None:
            print("Linked list is empty. Cannot delete head node.")
            return

        self.head = self.head.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

my_list = LinkedList()
my_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
my_list.head.next = second_node
second_node.next = third_node

print("Before deletion:")
my_list.print_list()

my_list.delete_head()

print("After deletion:")
my_list.print_list()
