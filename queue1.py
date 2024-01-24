import time

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
    
def isEmpty():
    global size
    if size==0:
        return True
    else:
        return False
    
def enQueue(tname):
    global rear,queue,size,front
    check=isFull()
    if check is False:
        if rear==4: # prevent rear being set over 4 out of index
            rear=-1
        queue[rear+1]=tname # enqueue the name in the next spot in the queue
        rear+=1
        size+=1
        print("\nFront=",front,"Rear=",rear,"Size=",size) # monitoring
        tablegen="""
              *********************
              * 0 * 1 * 2 * 3 * 4 *
              *********************
              * {0} * {1} * {2} * {3} * {4} *
              *********************"""
        print (tablegen.format(queue[0], queue[1],queue[2],queue[3],queue[4]))
        time.sleep(1)
    else:
        print("\nQueue is full, no more items can be enqueued")

def deQueue():
    global front,rear,queue,size
    check=isEmpty()
    if check is False:
        if front==5: # prevent front being set over 4 out of index
            front=0
        # queue[front]='' # dequeue the first item in the queue
        front+=1
        size-=1

        print("\nFront=",front,"Rear=",rear,"Size=",size) # monitoring
        tablegen="""
              *********************
              * 0 * 1 * 2 * 3 * 4 *
              *********************
              * {0} * {1} * {2} * {3} * {4} *
              *********************"""
        print(tablegen.format(queue[0], queue[1],queue[2],queue[3],queue[4]))
        time.sleep(1)
    else:
        print("\nQueue is empty, nothing to dequeue")

enQueue("A")
enQueue("B")
enQueue("C")
enQueue("D")
enQueue("E")
deQueue()
deQueue()
enQueue("F")
enQueue("G")
enQueue("H")
deQueue()
deQueue()
deQueue()
deQueue()
deQueue()
deQueue()

"""cont=True
while cont is True:
    name=input("name? ")
    if name=="end":
        cont=False
    else:
        enQueue(name)"""