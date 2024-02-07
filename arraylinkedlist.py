# linked list being stored as a 2d array. the first element of each inner array is the data for the "node",
# and the second element is the pointer for the next array according to the order the "nodes" are supposed to be in.
linkedList=[
    ["bob",3],
    ["sarah",2],
    ["sharon",None],
    ["roberto",1]
]

def traverse(list):
        head=0
        pointer=head
        while pointer!=None: # stops the list being traversed when it has reached the last element - inherently when its pointer is null
            print(list[pointer][0]) # prints the data for the node
            pointer=list[pointer][1] # assigns the address for the next node to be traversed using the pointer field of the current node

def insert(list):
      name=input("\n\nname to add? (not sorted)\n\n")
      head=0
      pointer=head
      added=False
      while added is not True: # case to stop attempts to carry on finding the last element when it has already been found
        if list[(list[pointer][1])][1]==None: # finds the pointer for the next element
                list.append([name,None]) # adds the new node to the array, assigns pointer of null as it has been added to the end of the list
                list[(list[pointer][1])][1]=(len(list)-1) # sets the next node's pointer to the position of the new node that we have just added
                added=True
                print(list)
        else:
              pointer=list[pointer][1] # sets the current pointer to the pointer of the next node
              print(pointer)

def sortInsert(list):
    name=input("\n\nname to add? (sorted)\n\n")
    head=-1
    pointer=head
    added=False
    while added is not True: # case to stop attempts to carry on finding the spot for the sorted item to be added after it has been added
        if pointer!=None: # won't allow the program to carry on searching for the right spot if there are no more nodes (end of list)
            if list[(list[pointer][1])][0]>name: # if the data of the next node is alphabetically "greater" than the inputted name
                # testing
                if pointer==-1:
                     oldPointer=list[pointer][1]
                     list.append([name,1])
                     added=True
                     print(list)
                # testing
                else:
                    oldPointer=list[pointer][1] # stores the pointer of the current node for reassignment to the newly-added node
                    list.append([name,oldPointer]) # the pointer of the newly-added node is set as the pointer of the current node to carry on the order
                    list[pointer][1]=(len(list)-1) # sets the pointer of the current node to the location of the newly-added node
                    added=True
                    print(list)
            else: # if the data of the next node is alphabetically "lower" than the inputted name, meaning it is not the right space for it to be added
                 pointer=list[pointer][1] # sets the current pointer to the pointer of the next node
                 print(pointer)
        else: # in the case that the inputted name is "lower" than the data for every single node in the list
                list.append([name,None]) # adds the node to the end, pointing to null as it is at the end
                list[(list[pointer][1])][1]=(len(list)-1) # sets the pointer of what was previously the last node to the newly-added node
                added=True
                print(list)


insert(linkedList)

traverse(linkedList)

sortInsert(linkedList)

traverse(linkedList)