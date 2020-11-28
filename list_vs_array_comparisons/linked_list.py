# A simple Python program for traversal of a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
#*********************************************INSERTION METHODS******************************************************************
    #Insertion METHOD (FROM HEAD)
    def insertfromHead(self, new_data):
        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node
        
    #INSERTION METHOD (FROM TAIL)
    def insertfromTail(self,new_data):
        #1-ALLOCATION AND PUTTING THE DATA
        new_node = Node(new_data)
        #iteration to find the last one
        #IF NODE WAS EMPTY
        if self.head is None:
            self.head = new_node
            return
        iter = self.head
        while(iter.next):
            iter = iter.next
        iter.next = new_node
    #INSERTION IN BETWEEN
    def insertAfter(self,prev_node,new_data):
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node

#*********************************************INSERTION METHODS******************************************************************
#**********************************************DELETION METHODS******************************************************************
    #DELETES HEAD
    def deleteHead(self):
        self.head = self.head.next

    #DELETES THE GIVEN KEY
    def deleteNode(self, key):  
          
        # Store head node  
        temp = self.head  
  
        # If head node itself holds the key to be deleted  
        if (temp is not None):  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
  
        # Search for the key to be deleted, keep track of the  
        # previous node as we need to change 'prev.next'  
        while(temp is not None):  
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
  
        # if key was not present in linked list  
        if(temp == None):  
            return
  
        # Unlink the node from linked list  
        prev.next = temp.next
  
        temp = None
    #DELETES THE TAIL
    def deleteTail(self):
        temp = self.head

        # If head node itself holds the key to be deleted  
        if (temp is not None):  
            if (temp.next is None):  
                self.head = temp.next
                temp = None
                return
        #GOING TO THE LAST NODE
        while(temp.next is not None):  
            prev = temp  
            temp = temp.next

        if(temp == None):  
            return
        # Unlink the node from linked list  
        prev.next = temp.next
  
        temp = None
#********************************************DELETING THE ENTIRE LINKED LIST********************************************
#1- Object-Oriented =)
    def deleteListOOP(self):
        while(self.head is not None):
            self.deleteTail()
#2- Deleting the Entire List
    def deleteList(self): 
        # initialize the current node 
        current = self.head 
        while current: 
            prev = current.next # move next node 
              
            # delete the current node 
            self.deleteNode(current.data) 
              
            # set current equals prev node 
            current = prev  
#**************************************************LENGTH OF THE LIST************************************************************
    def listLength(self):
        temp = self.head # Initialise temp 
        count = 0 # Initialise count 
    
        # Loop while end of linked list is not reached 
        while (temp): 
            count += 1
            temp = temp.next
        return count
#***************************************************GET THE MIDDLE ELEMENT********************************************************
    #SINCE ONE MOVES TWO STEP FASTER THAN THE OTHER ONE, BY THE TIME ONE FINISHES, THE OTHER IS IN THE HALF OF THE LIST
    def getMid(self, head): 
        if (head == None): 
            return head 
  
        mid = head 
        full = head 
  
        while (full.next != None and 
               full.next.next != None): 
            mid = mid.next
            full = full.next.next
              
        return mid 
#*************************************************SEARCH AN ELEMENT OF A LINKED LIST***********************************************
    def searchNode(self,key):
        temp = self.head
        #IF THE SEARCHED NODE IS HEAD
        if(self.head.data == key):
            return self.head
        #PROCEEDING TO FIND THE NODE
        while(temp is not None):  
            if temp.data == key:  
                return temp
            prev = temp  
            temp = temp.next

        if(temp == None):
            unfound = Node(-1)
            print("No data was found")  
            return unfound
#*********************************************GET THE NTH NODE*********************************************************
    def findNodeByIndex(self,index):
        temp = self.head
        count = 0

        while(temp is not None):  
            if count == index:  
                return temp  
            temp = temp.next
            count += 1
#*************************************************************REVERSING A LINKED LIST**********************************************
    #REVERSING THE LINKED LIST
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
#******************************************************************MERGE SORT*****************************************************
    def mergerLinkedList(self, l, r): 
        merged = None
        # IF HEADS ARE NONE 
        if l == None: 
            return r 
        if r == None: 
            return l  
        #COMPARISONS
        if l.data <= r.data: 
            merged = l 
            merged.next = self.mergerLinkedList(l.next, r) 
        else: 
            merged = r 
            merged.next = self.mergerLinkedList(l, r.next) 
        return merged 
      
    def mergeSort_linked_list(self, head):     
        #IF HEAD IS NONE
        if head is None or head.next is None: 
            return head 
        #MIDDLE ELEMENT
        mid = self.getMid(head) 
        nextmid = mid.next
        mid.next = None
        #RECURSION 
        left = self.mergeSort_linked_list(head) 
        right = self.mergeSort_linked_list(nextmid) 
        #MERGE
        sortedlist = self.mergerLinkedList(left, right) 
        return sortedlist
#************************************************************MERGESORT-LINKED-LIST**************************************************************