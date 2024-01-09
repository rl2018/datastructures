class Node():
    def __init__(self,theData):
        self.data=theData
        self.next=None

class LinkedList():
    def __init__(self,theHeadData):
        self.head=Node(theHeadData)

people=LinkedList("Sarah")

print(people)
print(people.head.next)