queue=['','','','',''] # initialising empty array

# initialising main variables
front=0
rear=-1
size=0

def isFull():
    global size
    if size==5:
        return True # if full
    else:
        return False # if not full
    
def enQueue(tname):
    global rear,queue,size,front
    if rear>4: # prevent rear being set over 4 out of index
        rear=0
    queue[rear+1]=tname # enqueue the name in the next spot in the queue
    rear+=1
    size+=1
    print("Front=",front,"Rear=",rear,"Size=",size) # monitoring
    print(queue)

def deQueue():
    global front,rear,queue,size
    queue[front]='' # dequeue the first item in the queue
    size-=1
    if front>4: # prevent front being set over 4 out of index
        front=0
    else:
        front+=1
    rear-=1
    print("Front=",front,"Rear=",rear,"Size=",size) # monitoring
    print(queue)

enQueue("A")
enQueue("B")
enQueue("C")
enQueue("D")
print(isFull())
enQueue("E")
deQueue()
deQueue()
enQueue("F")

"""cont=True
while cont is True:
    name=input("name? ")
    if name=="end":
        cont=False
    else:
        enQueue(name)"""