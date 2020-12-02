#********STACK CLASS*******************
#NODE*******************************
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
#NODE******************************
class Stack:
    def __init__(self):
        self.top = None

#***PRINTING THE STACK**********************************************

    def printStack(self):
        temp = self.top
        while(temp):
            print(temp.data)
            temp = temp.next

#***PRINTING THE STACK**********************************************
#***PUSHING*********************************************************
    def push(self,new_data):
        #CONSTRUCT A NEW NODE
        new_node = Node(new_data)
        #PUSH TO THE TOP 
        new_node.next = self.top
        self.top = new_node
#***PUSHING**********************************************************
#***POPPING**********************************************************
    def pop(self):
        if self.top is None:
            print("The stack is already empty")
            return
        #FOR MEMORY IN CASE IT IS NECESSARY
        #tmp = self.top
        #JUST PUSH THE NEXT ONE OUT**************************
        self.top = self.top.next
#***POPPING***********************************************************

