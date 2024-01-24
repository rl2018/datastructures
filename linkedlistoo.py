class Node():
    def __init__(self, given_data): # create node
        """Constructor method"""
        self.data=given_data
        self.next=None
    
    def get_data(self): # find the data associated with the node
        return self.data
    
    def get_next(self): # find the address of the next node
        return self.next
    
    def set_next(self,new_next): # set the address of the next node
        self.next=new_next

class LinkedList():
    def __init__(self): # create the linked list
        """Constructor method"""
        self.head=None

    def traverse(self):
        # set the current node as the head
        current=self.head

        #repeat until there are no more linked nodes
        while current is not None:
            print(current.get_data())
            current=current.get_next()

    def insert_at_front(my_list, data):
        # Create a new node
        new_node = NodeRecord()
        new_node.data = data

        # Check if the head node exists
        if my_list.head is None:
            my_list.head = new_node
        else:
            # Update the pointers so the new node is the head
            new_node.next = my_list.head           
            my_list.head = new_node

    def insert_at_front(self, data):
        # Create a new node
        new_node = Node(data)

        # Check if the head node exists
        if self.head is None:
            self.head = new_node
        else:
            # Update the pointers so the new node is the head
            new_node.set_next(self.head)            
            self.head = new_node

    def insert_in_order(my_list, data):
        
        # Create a new node
        new_node = NodeRecord()
        new_node.data = data

        # Start at the head of the list
        current = my_list.head

        # Check if there are no nodes in the list
        if current is None:
            my_list.head = new_node

        # Check if the new node data is before the head data
        elif new_node.data < current.data:
            # Set the new node as the head of the list
            new_node.next = my_list.head
            my_list.head = new_node

        # Otherwise find where the new node should be positioned
        else:
            # Repeat until the point of insertion is found
            while (current.next is not None
                and current.next.data < new_node.data):
                # Get the next node
                current = current.next
                
            # Update the pointers of the new and current nodes
            new_node.next = current.next
            current.next = new_node

    def insert_in_order(self, data):
        """Insert a node into the correct position in an ordered list"""

        # Create a new node
        new_node = Node(data)

        # Start at the head of the list
        current = self.head
        
        # Check if there are no nodes in the list
        if current is None:
            self.head = new_node

        # Check if the new node data is before the head data
        elif new_node.get_data() < current.get_data():
            # Set the new node as the head of the list
            new_node.set_next(self.head)
            self.head = new_node

        # Otherwise find where the new node should be positioned
        else:
            # Repeat until the point of insertion is found
            while (current.get_next() is not None
                  and current.get_next().get_data() < new_node.get_data()):
                # Get the next node
                current = current.get_next()

            # Update the pointers of the new and current nodes
            new_node.set_next(current.get_next())
            current.set_next(new_node)

# Instantiate an empty linked list object

my_list=LinkedList()

node1=Node("John")
print(node1.get_data())

node2=Node("Bob")

print(node2.get_data())

print(node1.get_next())

node1.set_next(node2)
print(node1.get_next())

