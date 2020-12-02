#THE QUEUE CLASS
#NODE*******************************
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
#NODE******************************
class Queue:
    def __init__(self):
        self.head = None

#***PRINTING THE QUEUE**********************************************

    def printQueue(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

#***PRINTING THE QUEUE**********************************************
#***ENQUEUE*********************************************************
    def enqueue(self,new_data):
        #CONSTRUCT A NEW NODE
        new_node = Node(new_data)
        #PUSH TO THE TOP
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        #GETTING TO THE TAIL
        while(temp.next):
            temp = temp.next
        temp.next = new_node
#***ENQUEUE**********************************************************
#***DEQUEUE**********************************************************
    def dequeue(self):
        if self.head is None:
            print("The queue is already empty")
            return
        #FOR MEMORY IN CASE IT IS NECESSARY
        #tmp = self.top
        #JUST PUSH THE NEXT ONE OUT**************************
        self.head = self.head.next
#***DEQUEUE***********************************************************
