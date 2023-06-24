class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

current_node = node1
while current_node is not None:
    print(current_node.data, end=" ")
    current_node = current_node.next
    '''Dynamic Code
     class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list():
    num_nodes = int(input("Enter the number of nodes: "))
    if num_nodes <= 0:
        print("Number of nodes should be greater than zero.")
        return None

    head = None
    current_node = None

    for i in range(num_nodes):
        data = input(f"Enter the value for node {i+1}: ")
        new_node = Node(data)

        if head is None:
            head = new_node
            current_node = head
        else:
            current_node.next = new_node
            current_node = new_node

    return head


def print_linked_list(head):
    if head is None:
        print("Linked list is empty.")
    else:
        current_node = head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next


linked_list = create_linked_list()

print("Linked list values:")
print_linked_list(linked_list)'''


