class Node():
    # Constructor method
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class Stack():
    def __init__(self):
        # Constructor method
        self.top = None

    def push(self, data):
        new_node = Node(data)
        # Check if the stack is NOT empty
        if not self.is_empty():
            # Point to the next element in the list
            new_node.set_next(self.top)
        # Set top to point to the new node
        self.top = new_node

    def pop(self):
        popped_data = None
        if self.is_empty():
            print("Stack is empty - nothing to pop")
        else:
            # Get data and change pointer to next item
            popped_data = self.top.get_data()
            self.top = self.top.get_next()
        return popped_data
    
    def peek(self):
        peeked_data = None
        if self.is_empty():
            print("Stack is empty - nothing to peek")
        else:
            # Get data from the top of the stack
            peeked_data = self.top.get_data()
        return peeked_data

    def is_empty(top):
        if top == -1:
            return True
        else:
            return False
        

stack1=Stack()
print(stack1.peek())
stack1.push("Mondeo")
print(stack1.peek())
stack1.push("Golf")
print(stack1.peek())
stack1.pop()
stack1.pop()