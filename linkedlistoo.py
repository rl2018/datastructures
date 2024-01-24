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
        #set the current node as the head
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

# Instantiate an empty linked list object

my_list=LinkedList()
