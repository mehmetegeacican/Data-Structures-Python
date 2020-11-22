# for Garbage collection
import gc
#THIS IS THE DOUBLE LINKED LIST 
#NODE
class Node:
    def __init__(self,prev= None,next=None,data =None):
        self.next = next #NEXT OF DLL
        self.prev = prev #PREV OF DLL
        self.data = data #DATA OF DLL


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    #PRINT THE LIST(FROM HEAD TO TAIL)
    def printList(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next
   
    #INSERT HEAD
    def insertHead(self,new_data):
        #ALLOCATE NEW NODE
        new_node = Node(data = new_data)
        new_node.prev = None
        new_node.next = self.head
       #change prev of head node to new node  
        if self.head is not None: 
            self.head.prev = new_node
       #ASSIGN NEW NODE TO BE HEAD
        self.head = new_node
    #INSERT TAIL
    def insertTail(self,new_data):
        #ALLOCATE NEW NODE
        new_node = Node(data = new_data)
        new_node.next = None
        #IF LINKED LIST WAS EMPTY
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
        else:
            #ITERATING TO THE LAST LINKED LIST
            tmp = self.head
            while(tmp.next):
                tmp = tmp.next
            #ADJUSTING THE LINKED LIST
            tmp.next = new_node
            new_node.prev = tmp
            return
    #INSETING TO THE SPECIFIC PLACE
    def insertIndex(self,new_data,prev_node):

        #PRECAUTION: THE PREV NODE CAN NOT BE EMPTY
        if prev_node is None: 
            print("the given previous node cannot be NULL")
            return 
        #ALLOCATE THE NEW NODE
        new_node = Node(data = new_data)
        #PLACING THE NEW NODE
        new_node.next = prev_node.next
        prev_node.next = new_node

        # CHANGE THE PREVIOUS OF NEW NODES
        if new_node.next is not None: 
            new_node.next.prev = new_node

    def deleteNode(self, dele):
         
        # Base Case
        if self.head is None or dele is None:
            return
         
        # If node to be deleted is head node
        if self.head == dele:
            self.head = dele.next
 
        # Change next only if node to be deleted is NOT
        # the last node
        if dele.next is not None:
            dele.next.prev = dele.prev
     
        # Change prev only if node to be deleted is NOT 
        # the first node
        if dele.prev is not None:
            dele.prev.next = dele.next
        # Finally, free the memory occupied by dele
        # Call python garbage collector
        gc.collect()




           

